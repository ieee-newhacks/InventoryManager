from flask import Flask, render_template, Markup, request, redirect, url_for # For flask
from bson import ObjectId # for ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)

title = "SYDE Order: An Inventory Manager for retailers to determine what's hot and what's not."
heading = "SYDE Order"

client = MongoClient("mongodb+srv://sydemans:sydemans123@cluster0-qcrqx.mongodb.net/test?retryWrites=true")
db = client.Inventory
clothes = db.tshirt


@app.route('/', methods=['GET'])
def home(): 
    if request.method=='GET':
        return render_template('/index.html')
    else:
        return render_template('/index.html')
