from flask import Flask
from flask import request, redirect, url_for
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
from model import todo

app = Flask(__name__)

tod= todo.Todo()
"""
def checuser(name):
    if collection.find_one({"name": name}):
        return False
    else:
        return True

"""
"""
@app.route("/addUser", methods=["POST"])
def adduser():
    request_payload = request.get_json(force=True)
  #  print(checuser(request_payload["name"]))
    if checuser(request_payload["name"]):
        collection.insert_one({"name": request_payload["name"], "tasks": {}})
        return "added User"
    else:
        return "User exist"
"""


@app.route("/addTask", methods=["POST"])
def addtask():
    request_payload = request.get_json(force=True)

    task = request_payload["task"]
    """
    #str = f"tasks.{task}"
    #myquery = {"name": request_payload["name"]}
    #newvalues = {"$set":
     #                    {
      #                       str: False
       #                  }
        #             }
    #collection.update_one(myquery, newvalues)
    """
    return json.dumps(tod.add(task))


@app.route("/getTask")
def getTask():
    #request_payload = request.get_json(force=True)
    #print(request_payload)

    return json_util.dumps(tod.get())


@app.route("/markTaskComplete", methods=["POST"])
def marktaskcomplete():
    request_payload = request.get_json(force=True)

    if "task" in request_payload:
        task = request_payload["task"]
        #str = f"tasks.{task}"

        return tod.markcomp(task)
    else:
        return redirect(url_for('getTask'))
            

if __name__ == "__main__":
    app.run()
