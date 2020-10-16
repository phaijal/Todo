from model import copytodo
import json
from bson import json_util


class Controller:
    def add_heading(self, request_payload):
        heading = request_payload["heading"]
        copytodo.add_heading(heading)


    def get_heading(self):
        t = copytodo.get_all_task_object()
        ret = []
        for a in t:
            ret.append(a.heading)
        return json.dumps(ret)


    def add_task(self, request_payload):
        heading = request_payload["heading"]
        task = request_payload["task"]
        #copytodo.add_task(heading, task)
        task_name = copytodo.taskname(task=task, done=False)
        t = copytodo.get_task_object(heading)
        t.tasks.append(task_name)
        copytodo.save_task_object(t)


    def get_Task(self, heading):
        t = copytodo.get_task_object(heading)
        tasks = list(t.tasks)
        print(tasks)
        ret = []
        for a in tasks:
            ret.append(a.task)
        return json.dumps(ret)


    def mark_taskcomplete(self, request_payload):
        if "heading" in request_payload:
            if "task" in request_payload :
                heading = request_payload["heading"]
                task = request_payload["task"]
              #  copytodo.mark_complete(heading, task)
                t = copytodo.get_task_object(heading)
                for a in t.tasks:
                    if a.task == task:
                        a.done = True
                copytodo.save_task_object(t)
                ret_json = {
                    "msg": f"{task}, status: Completed"
                }
                return json.dumps(ret_json)
            else:
                ret_json = {
                    "msg": "no task specified"
                }
                return json.dumps(ret_json)
        else:
            ret_json = {
                "msg": "no heading specified"
            }
            return json.dumps(ret_json)
