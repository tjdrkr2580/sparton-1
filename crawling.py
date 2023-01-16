from flask import Flask, render_template, request, jsonify

import requests
from bs4 import BeautifulSoup

from db import db

def movies_post():
    url_receive = request.form['url_give']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)


    try :
        soup = BeautifulSoup(data.text, 'html.parser')


        title = soup.select_one('meta[property="og:title"]')['content']
        image = soup.select_one('meta[property="og:image"]')['content']
        desc = soup.select_one('meta[property="og:description"]')['content']
        star = soup.select_one('#actualPointPersentBasic > div > span > span')
        director = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')
        movie_list = list(db.movies.find({}, {'_id': False}))
        count = len(movie_list) + 1

        # content > div.article > div.mv_info_area
        # actualPointPersentBasic > div

        doc = {
            'm_id' : count,
            'title': title,
            'image': image,
            'desc': desc,
            'star': float(star.text[-5:-1]),
            'director': director.text
        }

        db.movies.insert_one(doc)

        return jsonify({'msg': '저장 완료!'})
    except :
        return "error"
