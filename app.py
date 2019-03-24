from flask import Flask, render_template, Markup, request, redirect, url_for # For flask
from bson import ObjectId # for ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "SYDE Order: An Inventory Manager for retailers to determine what's hot and what's not."
heading = "SYDE Order"

client = MongoClient("mongodb+srv://sydemans:sydemans123@cluster0-qcrqx.mongodb.net/test?retryWrites=true")
db = client.inventory
tshirt = db.tshirt
longsleeves = db.longsleeves
jackets = db.jackets
jeans = db.jeans
shorts = db.shorts
footwear = db.footwear

@app.route('/',methods=['GET'])
@app.route("/index", methods=['GET'])
def home(): 
    # T-shirt Info
    tshirt_stock = tshirt.find({"CurrentStock":120})
    tshirt_current = tshirt.find({"CurrentMonthlySales":80})
    tshirt_prev = tshirt.find({"PrevMonthlySales":70})

    # Longsleeves Info
    longsleeves_stock = longsleeves.find({"CurrentStock":230})
    longsleeves_current = longsleeves.find({"CurrentMonthlySales":70})
    longsleeves_prev = longsleeves.find({"PrevMonthlySales":50})

    # Jackets Info
    jackets_stock = jackets.find({"CurrentStock":36})
    jackets_current = jackets.find({"CurrentMonthlySales":13})
    jackets_prev = jackets.find({"PrevMonthlySales":45})

    # Jeans Info
    jeans_stock = jeans.find({"CurrentStock":450})
    jeans_current = jeans.find({"CurrentMonthlySales":195})
    jeans_prev = jeans.find({"PrevMonthlySales":234})

    # Shorts Info
    shorts_stock = shorts.find({"CurrentStock":80})
    shorts_current = shorts.find({"CurrentMonthlySales":35})
    shorts_prev = shorts.find({"PrevMonthlySales":50})

    # Footwear Info
    footwear_stock = footwear.find({"CurrentStock":187})
    footwear_current = footwear.find({"CurrentMonthlySales":55})
    footwear_prev = footwear.find({"PrevMonthlySales":34})

    return render_template('index.html', tshirtStock = tshirt_stock, tshirtCurrent = tshirt_current, tshirtPrev = tshirt_prev, longsleevesStock = longsleeves_stock, longsleevesCurrent = longsleeves_current, longsleevesPrev = longsleeves_prev, jacketsStock = jackets_stock, jacketsCurrent = jackets_current, jacketsPrev = jackets_prev, jeansStock = jeans_stock, jeansCurrent = jeans_current, jeansPrev = jeans_prev, shortsStock = shorts_stock, shortsCurrent = shorts_current, shortsPrev = shorts_prev, footwearStock = footwear_stock, footwearCurrent = footwear_current, footwearPrev = footwear_prev)

if __name__ == '__app__':
        app.run(debug=True)