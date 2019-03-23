import requests
import random
from datetime import datetime
from pymongo import MongoClient


from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
title = "Inventory Manager"

client = MongoClient("mongodb+srv://sydemans:sydemans123@cluster0-qcrqx.mongodb.net/test?retryWrites=true")
db = client.Inventory
todos = db.Manager

print(client.mflix)

@app.route("/", methods=['GET'])
@app.route('/mainmenu',methods=['GET'])
def hello():
    return "<h1>Hello World!<h1>"