from flask import Flask
from flask import request
import json

from controller import contro
app = Flask(__name__)

c = contro.Controller()


@app.route("/Heading", methods=["POST"])
def addHeading():
    request_payload = request.get_json(force=True)
    c.add_heading(request_payload)
    ret_json = {
        "msg": "Added Heading"
    }
    return json.dumps(ret_json)


@app.route("/Heading")
def getheading():
    return c.get_heading()


@app.route("/Task/<heading>", methods=["GET"])
def getTask(heading):
    #request_payload = request.get_json(force=True)
    #heading = request_payload["heading"]
    return c.get_Task(heading)


@app.route("/Task/<heading>", methods=["POST"])
def addtask(heading):
    request_payload = request.get_json(force=True)
    c.add_task(heading,request_payload)
    ret_json = {
        "msg": "Added Task"
    }
    return json.dumps(ret_json)


@app.route("/markTaskComplete/<heading>", methods=["POST"])
def marktaskcomplete(heading):
    request_payload = request.get_json(force=True)
    return c.mark_taskcomplete(heading,request_payload)


if __name__ == "__main__":
    app.run()
