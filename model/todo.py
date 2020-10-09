import pymongo
from pymongo import MongoClient
import json
cluster = MongoClient("mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["dbname"]
collection = db["coll"]


class Todo(object):
    def add(self, task):
        collection.insert_one({"task": task, "done": False})
        ret_json = {
            "msg": "Added Task"
        }
        return ret_json

    def get(self):
        return collection.find({}, {"task": 1, "done": 1, "_id": 0})

    def markcomp(self,task):
        myquery = {"task": task}
        newvalues = {"$set":
            {
                "done": True
            }
        }
        collection.update_one(myquery, newvalues)
        ret_json = {
            "msg": f"{task}, status: Completed"
        }
        return ret_json
