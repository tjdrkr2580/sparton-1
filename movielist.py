from flask import jsonify
from db import db


#영화 리스트 불러오기
def movie_list():
    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies': movie_list})
