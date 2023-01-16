from flask import jsonify, render_template, request
from db import db


@app.route("/comments", method=["GET"])
def comments_get():
    comments_list = list(db.comments.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})


@app.route("/comments", methods=["POST"])
def comment_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]
    num_receive = request.form['m_id_give']

    doc = {
        'm_id': num_receive,
        'c_id': name_receive,
        'comment': comment_receive
    }

    db.comments.insert_one(doc)
    return jsonify({'msg': '댓글 완료!'})
