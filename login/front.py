from flask_restful import Resource, Api, reqparse
from flask import Flask, request, jsonify
from modellogin import *
import sys
sys.path.append('../')
from model import copytodo

def funct(user):
    val = 0
    for a in user:
        val += ord(a)
    return val
class register(Resource):
    def post(self):
        response = request.get_json(force=True)
        inform = info(Age=response['info']['Age'], Born=response['info']['Born'])

        registering = User(Username=response['username'], information=inform)
        registering.Password = funct(response['password'])
        registering.save()
        copytodo.add_people(response['username'])
        return "succesfully registered"


"""
from flask_restful import Resource, Api , reqparse
from flask import Flask, request , jsonify
from modellogin import *
import sys
sys.path.append('../')
from model import copytodo
#ctodo = copytodo()
class register(Resource):
    def post(self):
        response = request.get_json(force=True)
       # print(response)
        inform = info(Age =response['info']['Age'], Born = response['info']['Born'])
        registering = User(Username=response['username'], Password=response['password'],information=inform).save()
        copytodo.add_people(response['username'])
        return "succesfully registered"
"""

