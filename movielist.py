from flask import jsonify, request
from db import db
from bs4 import BeautifulSoup

#영화 리스트 불러오기
def movie_list():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies': movie_list})

#리스트에 영화 추가하기
def add_movie():
    url_receive = request.form['url_give']

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url_receive, headers=headers)
    #
    # soup = BeautifulSoup(data.text, 'html.parser')
    #
    # title = soup.select_one('meta[property="og:title"]')['content']
    # image = soup.select_one('meta[property="og:image"]')['content']
    # desc = soup.select_one('meta[property="og:description"]')['content']

    movie_list = list(db.movies.find({}, {'_id': False}))
    count = len(movie_list) + 1

    doc = {
        'm_id': count,
        'm_star': m_star_receive,
        'm_link': m_link_receive
    }

    db.movies.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})
