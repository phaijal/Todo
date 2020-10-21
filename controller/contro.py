from model import copytodo
import json
from bson import json_util
import jwt
from login import modellogin

def auth(payload):
    try:

        for user in modellogin.User.objects:
            if user.Username == payload['sub']:
                return 1
                break



    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'

    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


class Controller:
    def add_heading(self, request_payload,payload):
        authmsg = auth(payload)
        if authmsg == 1 :

            heading = request_payload["heading"]
            copytodo.add_heading(payload['sub'],heading)
            ret_json = {
                "msg": "Added Heading"
            }
        else:
            ret_json= {
                "msg": authmsg
            }
        return ret_json


    def get_heading(self,payload):
        ret = []
        lis = list(copytodo.get_heading(payload['sub']).section)
        for a in lis:
            ret.append(a.heading)
        return json.dumps(ret)


    def add_task(self,heading, request_payload,payload):
        #heading = request_payload["heading"]
        task = request_payload["task"]
        #copytodo.add_task(heading, task)
        task_name = copytodo.taskname(task=task, done=False)
        p = copytodo.get_task_object(payload['sub'])
        for a in p.section:
            if a.heading == heading:
                a.tasks.append(task_name)
        p.save()

    def get_Task(self, heading,payload):
        p = copytodo.get_task_object(payload['sub'])
        ret = []
        for a in p.section:
            if a.heading == heading:
                for t in a.tasks:
                    ret.append(t.task)

        return ret


    def mark_taskcomplete(self,heading, request_payload,payload):

        if "task" in request_payload :
            task = request_payload["task"]
            p = copytodo.get_task_object(payload['sub'])
            for a in p.section:
                if a.heading == heading:
                    for t in a.tasks:
                        if t.task == task:
                            t.done = True
                            break
            p.save()
            m = task+", status: Completed"
            ret_json = {
                "msg": m
            }
            return ret_json
        else:
            ret_json = {
                "msg": "no task specified"
            }
            return ret_json

