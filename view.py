from flask import Flask
from flask import request
import json
import jwt

from controller import contro
app = Flask(__name__)

c = contro.Controller()


@app.route("/Heading", methods=["POST"])
def addHeading():
    request_payload = request.get_json(force=True)
    ret_json = c.add_heading(request_payload,jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))

    return json.dumps(ret_json)


@app.route("/Heading")
def getheading():
    return c.get_heading(jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))


@app.route("/Task/<heading>", methods=["GET"])
def getTask(heading):
    #request_payload = request.get_json(force=True)
    #heading = request_payload["heading"]
    return json.dumps(list(c.get_Task(heading,jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))))


@app.route("/Task/<heading>", methods=["POST"])
def addtask(heading):
    request_payload = request.get_json(force=True)
    c.add_task(heading,request_payload,jwt.decode(request.headers['Authorization'], key, algorithms='HS256'))
    ret_json = {
        "msg": "Added Task"
    }
    return json.dumps(ret_json)


@app.route("/markTaskComplete/<heading>", methods=["POST"])
def marktaskcomplete(heading):
    request_payload = request.get_json(force=True)
    return json.dumps(c.mark_taskcomplete(heading,request_payload,jwt.decode(request.headers['Authorization'], key, algorithms='HS256')))



#LOGIN API
from flask import Flask, request , jsonify

from flask_restful import Resource, Api , reqparse

from login.front import *
from login.controller import *
#app = Flask(__name__)
key = 'secret'

api= Api(app)

# if password has special characters we need to encode them
#connect(host ="mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/dbname?retryWrites=true&w=majority")

#view
api.add_resource(register,'/register')


api.add_resource(login,'/login')


api.add_resource(info,'/info')



if __name__ == "__main__":
    app.run()


