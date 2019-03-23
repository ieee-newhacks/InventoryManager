from flask import Flask, render_template, Markup, request, redirect
from config import col, col_results
import requests
import random

app = Flask(__name__)


@app.route('/', method=['GET'])
def home(): 
    return render_template('/index.html')
