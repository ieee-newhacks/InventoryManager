from flask import Flask, render_template, Markup, request, redirect, url_for # For flask
from bson import ObjectId # for ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "SYDE Order: An Inventory Manager for retailers to determine what's hot and what's not."
heading = "SYDE Order"

client = MongoClient("mongodb+srv://sydemans:sydemans123@cluster0-qcrqx.mongodb.net/test?retryWrites=true")

@app.route('/',methods=['GET'])
@app.route("/index", methods=['GET'])
def home(): 
    # T-shirt Info
    tshirts = [40, 80, 70]
    sales_trend_tshirts = (tshirts[1] - tshirts[2]) / tshirts[2] * 100
    reco_tshirt_qty = (tshirts[1] - tshirts[0]) + 20

    #Longsleeves Info
    longsleeves = [50, 70, 50]
    sales_trend_longsleeves = (longsleeves[1] - longsleeves[2]) / longsleeves[2] * 100
    reco_longsleeves_qty = (longsleeves[1] - longsleeves[0]) + 20

    #Jackets Info
    jackets = [13, 36, 45]
    sales_trend_jackets = (jackets[1] - jackets[2]) / jackets[2] * 100
    reco_jackets_qty = (jackets[1] - jackets[0]) + 20

    #Jeans Info
    jeans = [40, 195, 234]
    sales_trend_jeans = (jeans[1] - jeans[2]) / jeans[2] * 100
    reco_jeans_qty = (jeans[1] - jeans[0]) + 20

    #Shorts Info
    shorts = [29, 50, 35]
    sales_trend_shorts = (shorts[1] - shorts[2]) / shorts[2] * 100
    reco_shorts_qty = (shorts[1] - shorts[0]) + 20

    #Footwear Info
    footwear = [78, 56, 91]
    sales_trend_footwear = (footwear[1] - footwear[2]) / footwear[2] * 100
    reco_footwear_qty = (footwear[1] - footwear[0]) + 25

    # WOMEN's Database

    #W T-shirt Info
    wtshirts = [67, 94, 86]
    wsales_trend_tshirts = (wtshirts[1] - wtshirts[2]) / wtshirts[2] * 100
    wreco_tshirt_qty = (wtshirts[1] - wtshirts[0]) + 20

    #W Longsleeves Info
    wlongsleeves = [30, 25, 34]
    wsales_trend_longsleeves = (wlongsleeves[1] - wlongsleeves[2]) / wlongsleeves[2] * 100
    wreco_longsleeves_qty = (wlongsleeves[1] - wlongsleeves[0]) + 20

    #W Jackets Info
    wjackets = [37, 65, 54]
    wsales_trend_jackets = (wjackets[1] - wjackets[2]) / wjackets[2] * 100
    wreco_jackets_qty = (wjackets[1] - wjackets[0]) + 20

    #W Jeans Info
    wjeans = [205, 150, 147]
    wsales_trend_jeans = (wjeans[1] - wjeans[2]) / wjeans[2] * 100
    wreco_jeans_qty = (wjeans[1] - wjeans[0]) + 20

    #W Skirts Info
    wskirts = [67, 54, 30]
    wsales_trend_skirts = (wskirts[1] - wskirts[2]) / wskirts[2] * 100
    wreco_skirts_qty = (wskirts[1] - wskirts[0]) + 20

    #W Footwear Info
    wfootwear = [145, 78, 94]
    wsales_trend_footwear = (wfootwear[1] - wfootwear[2]) / wfootwear[2] * 100
    wreco_footwear_qty = (wfootwear[1] - wfootwear[0]) + 20

    return render_template('index.html', tshirts = tshirts, sales_tshirts = round(sales_trend_tshirts), reco_tshirts = reco_tshirt_qty, longsleeves = longsleeves, sales_longsleeves = round(sales_trend_longsleeves), reco_longsleeves = reco_longsleeves_qty, jackets = jackets, sales_jackets = round(sales_trend_jackets), reco_jackets = reco_jackets_qty, jeans = jeans, sales_jeans = round(sales_trend_jeans), reco_jeans = reco_jeans_qty, shorts = shorts, sales_shorts = round(sales_trend_shorts), reco_shorts = reco_shorts_qty, footwear = footwear, sales_footwear = round(sales_trend_footwear), reco_footwear = reco_footwear_qty, wtshirts = wtshirts, wsales_tshirts = round(wsales_trend_tshirts), wreco_tshirts = wreco_tshirt_qty, wlongsleeves = wlongsleeves, wsales_longsleeves = round(wsales_trend_longsleeves), wreco_longsleeves = wreco_longsleeves_qty, wjackets = wjackets, wsales_jackets = round(wsales_trend_jackets), wreco_jackets = wreco_jackets_qty, wjeans = wjeans, wsales_jeans = round(wsales_trend_jeans), wreco_jeans = wreco_jeans_qty, wskirts = wskirts, wsales_skirts = round(wsales_trend_skirts), wreco_skirts = wreco_skirts_qty, wfootwear = wfootwear, wsales_footwear = round(wsales_trend_footwear), wreco_footwear = wreco_footwear_qty)

if __name__ == '__app__':
        app.run(debug=True)