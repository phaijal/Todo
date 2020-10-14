from flask import Flask
from flask import request, redirect, url_for
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
from model import todo, copytodo

app = Flask(__name__)

tod = todo.Todo()



@app.route("/addTask", methods=["POST"])
def addtask():
    request_payload = request.get_json(force=True)
    task = request_payload["task"]
    copytodo.add_task(task)
    ret_json = {
        "msg": "Added Task"
    }
    return json.dumps(ret_json)


@app.route("/getTask")
def getTask():
    return json_util.dumps(copytodo.get_tasks())


@app.route("/markTaskComplete", methods=["POST"])
def marktaskcomplete():
    request_payload = request.get_json(force=True)

    if "task" in request_payload:
        task = request_payload["task"]
        copytodo.mark_complete(task)
        ret_json = {
            "msg": f"{task}, status: Completed"
        }
        return json.dumps(ret_json)
    else:
        return redirect(url_for('getTask'))


if __name__ == "__main__":
    app.run()
