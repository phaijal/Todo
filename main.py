from flask import Flask
from flask import request
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

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
        collection.insert_one({"name": request_payload["name"], "tasks": []})
        return "added User"
    else:
        return "User exist"


@app.route("/addTask", methods=["POST"])
def addtask():
    request_payload = request.get_json(force=True)
    if checuser(request_payload["name"]):
        return "No such User"
    else:
        myquery = {"name": request_payload["name"]}
        newvalues = {"$push":
                         {
                             "tasks": request_payload["task"],
                              "done": False
                         }
                     }
        collection.update_one(myquery, newvalues)
        return "Added Task"








if __name__ == "__main__":
    app.run()