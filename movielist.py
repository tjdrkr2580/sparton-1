from flask import jsonify, request
from db import db


#영화 리스트 불러오기
def movie_list():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies': movie_list})

#리스트에 영화 추가하기
def add_movie():
    m_id_receive = request.form['m_id_give']
    m_star_receive = request.form['m_star_give']
    m_link_receive = request.form['m_link_give']

    doc = {
        'm_id' = m_id_receive,
        'm_star' = m_star_receive,
        'm_link' = m_link_receive
    }

    db.movies.insert_one(doc)

