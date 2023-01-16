from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')