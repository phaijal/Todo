from model import copytodo
import json
from bson import json_util


class Controller:
    def add_heading(self, request_payload):
        heading = request_payload["heading"]
        copytodo.add_heading(heading)

    def add_task(self, request_payload):
        heading = request_payload["heading"]
        task = request_payload["task"]
        copytodo.add_task(heading, task)


    def mark_taskcomplete(self, request_payload):
        if "heading" in request_payload:
            if "task" in request_payload :
                heading = request_payload["heading"]
                task = request_payload["task"]
                copytodo.mark_complete(heading, task)
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
"""      
    def add_task(self, request_payload):
        task = request_payload["task"]
        copytodo.add_task(task)

    def get_Task(self):
        return json_util.dumps(copytodo.get_tasks())

    def mark_taskcomplete(self, request_payload):

        if "task" in request_payload:
            task = request_payload["task"]
            copytodo.mark_complete(task)
            ret_json = {
                "msg": f"{task}, status: Completed"
            }
            return json.dumps(ret_json)
        else:
            ret_json = {
                "msg": "no task specified"
            }
            return json.dumps(ret_json)
"""