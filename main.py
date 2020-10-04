from flask import Flask
from flask import request, redirect, url_for
import pymongo
from pymongo import MongoClient
import json



app = Flask(__name__)
cluster = MongoClient("mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["dbname"]
collection = db["coll"]


def checuser(name):
    if collection.find_one({"name": name}):
        return False
    else:
        return True


@app.route("/addUser", methods=["POST"])
def adduser():
    request_payload = request.get_json(force=True)
  #  print(checuser(request_payload["name"]))
    if checuser(request_payload["name"]):
        collection.insert_one({"name": request_payload["name"], "tasks": {}})
        return "added User"
    else:
        return "User exist"




@app.route("/addTask", methods=["POST"])
def addtask():
    request_payload = request.get_json(force=True)
    if checuser(request_payload["name"]):
        return "No such User"
    else:
        task=request_payload["task"]
        str = f"tasks.{task}"
        myquery = {"name": request_payload["name"]}
        newvalues = {"$set":
                         {
                             str: False
                         }
                     }
        collection.update_one(myquery, newvalues)
        return "Added Task"


@app.route("/getTask", methods=["POST"])
def getTask():
    request_payload = request.get_json(force=True)
    if checuser(request_payload["name"]):
        return "No such User"
    else:
        val = collection.find_one({"name": request_payload["name"]})["tasks"]

        return json.dumps(val)

@app.route("/markTaskComplete", methods=["POST"])
def msrktaskcomplete():
    request_payload = request.get_json(force=True)
    if checuser(request_payload["name"]):
        return "No such User"
    else:
        #task = request_payload["task"]
        if "task" in request_payload:
            pass
        else:
            return redirect(url_for('getTask'),code=307)
            

            








if __name__ == "__main__":
    app.run()