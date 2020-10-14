from flask import Flask
from flask import request
import json

from controller import contro
app = Flask(__name__)

c = contro.Controller()


@app.route("/addTask", methods=["POST"])
def addtask():
    request_payload = request.get_json(force=True)
    c.add_task(request_payload)
    ret_json = {
        "msg": "Added Task"
    }
    return json.dumps(ret_json)


@app.route("/getTask")
def getTask():
    return c.get_Task()


@app.route("/markTaskComplete", methods=["POST"])
def marktaskcomplete():
    request_payload = request.get_json(force=True)
    return c.mark_taskcomplete(request_payload)


if __name__ == "__main__":
    app.run()
