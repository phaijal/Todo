from model import copytodo
import json
from bson import json_util


class Controller:
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
