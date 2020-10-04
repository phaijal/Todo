from flask import Flask
from flask import request
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)
cluster = MongoClient("mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = cluster["dbname"]
collection = db["copill"]


def checuser(name)
    if collection.find({}).length==0 :
        return True
    else:
        return False


@app.route("/addUser", methods=["POST"])
def adduser():
    request_payload = request.get_json(force=True)
    if checuser(request_payload["name"]) :
        collection.insert_one({"name": request_payload["name"]})










if __name__ == "__main__":
    app.run()