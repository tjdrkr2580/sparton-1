from flask import jsonify, render_template, request
from db import db


def comments_get():
    comments_list = list(db.comments.find({}, {'_id': False}))
    return jsonify({'comments': comments_list})


def comment_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]
    num_receive = request.form['m_id_give']
    password_receive = request.form['password_give']
    date_receive = request.form['date_give']
    comments_list = list(db.comments.find({}, {'_id': False}).sort('c_num'))
    # count = len(comments_list) + 1

    # user_list = list(db.comments.find({}, {'_id': False})

    last_comments_num = comments_list[-1]['c_num'] if len(comments_list) > 0 else 1

    doc = {
        'm_id': num_receive,
        'c_id': name_receive,
        'c_num': last_comments_num + 1,
        'comment': comment_receive,
        'password': password_receive,
        'date': date_receive
    }

    db.comments.insert_one(doc)
    return jsonify({'msg': '댓글 완료!'})



def comment_del():
    c_num_receive = request.form['c_num_give']
    password_receive = request.form['password']
    # db.comments_list

    # user = db.users.find_one({'id': id_receive}, {'_id': False})

    comment = db.comments.find_one({'c_num': int(c_num_receive)}, {'_id': False})

    if comment['password'] == password_receive :
        db.comments.delete_one({'c_num': int(c_num_receive)})
        return jsonify({'delete':'success', 'msg': '삭제 성공'})
    else :
        return jsonify({'delete':'fail', 'msg': '비밀번호가 틀립니다!'})


    #
    # comments_list = list(db.comments.find({}, {'_id': False}))

    # index = 0;
    # for i in comments_list:
    #     index += 1
    #     rows = i['num']
    #     db.bucket.update_one({'num': rows}, {'$set': {'num': index}});




