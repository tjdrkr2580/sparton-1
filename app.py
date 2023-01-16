from flask import Flask, render_template, request, jsonify
from movielist import movie_list
from crawling import movies_post

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


# 영화 목록 전체 조회 api
@app.route('/movies', methods=["GET"])
def movie_list_api():
  msg = movie_list()
  return msg

# 영화 추가 api
@app.route('/movies', methods=["POST"])
def movies_post_api():
  msg = movies_post()
  return msg


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)