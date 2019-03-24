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


@app.route('/index', methods=['GET'])
def home(): 
    # T-shirt Info
    tshirt_stock = tshirt.distinct("CurrentStock")
    tshirt_current = tshirt.distinct("CurrentMonthlySales")
    tshirt_prev = tshirt.distinct("PrevMonthlySales")

    # Longsleeves Info
    longsleeves_stock = longsleeves.distinct("CurrentStock")
    longsleeves_current = longsleeves.distinct("CurrentMonthlySales")
    longsleeves_prev = longsleeves.distinct("PrevMonthlySales")

    # Jackets Info
    jackets_stock = jackets.distinct("CurrentStock")
    jackets_current = jackets.distinct("CurrentMonthlySales")
    jackets_prev = jackets.distinct("PrevMonthlySales")

    # Jeans Info
    jeans_stock = jeans.distinct("CurrentStock")
    jeans_current = jeans.distinct("CurrentMonthlySales")
    jeans_prev = jeans.distinct("PrevMonthlySales")

    # Shorts Info
    shorts_stock = shorts.distinct("CurrentStock")
    shorts_current = shorts.distinct("CurrentMonthlySales")
    shorts_prev = shorts.distinct("PrevMonthlySales")

    # Footwear Info
    footwear_stock = footwear.distinct("CurrentStock")
    footwear_current = footwear.distinct("CurrentMonthlySales")
    footwear_prev = footwear.distinct("PrevMonthlySales")

    return render_template('index.html', tshirtStock = tshirt_stock, tshirtCurrent = tshirt_current, tshirtPrev = tshirt_prev, longsleevesStock = longsleeves_stock, longsleevesCurrent = longsleeves_current, longsleevesPrev = longsleeves_prev, jacketsStock = jackets_stock, jacketsCurrent = jackets_current, jacketsPrev = jackets_prev, jeansStock = jeans_stock, jeansCurrent = jeans_current, jeansPrev = jeans_prev, shortsStock = shorts_stock, shortsCurrent = shorts_current, shortsPrev = shorts_prev, footwearStock = footwear_stock, footwearCurrent = footwear_current, footwearPrev = footwear_prev)

if __name__ == '__app__':
        app.run(debug=True)