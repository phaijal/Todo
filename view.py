from flask import Flask
from flask import request
import json

from controller import contro
app = Flask(__name__)

c = contro.Controller()


@app.route("/addHeading", methods=["POST"])
def addHeading():
    request_payload = request.get_json(force=True)
    c.add_heading(request_payload)
    ret_json = {
        "msg": "Added Heading"
    }
    return json.dumps(ret_json)


@app.route("/getHeading")
def getheading():
    return c.get_heading()


@app.route("/getTask", methods=["POST"])
def getTask():
    request_payload = request.get_json(force=True)
    heading = request_payload["heading"]
    return c.get_Task(heading)


@app.route("/addTask", methods=["POST"])
def addtask():
    request_payload = request.get_json(force=True)
    c.add_task(request_payload)
    ret_json = {
        "msg": "Added Task"
    }
    return json.dumps(ret_json)


@app.route("/markTaskComplete", methods=["POST"])
def marktaskcomplete():
    request_payload = request.get_json(force=True)
    return c.mark_taskcomplete(request_payload)


if __name__ == "__main__":
    app.run()
