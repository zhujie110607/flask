from flask import render_template, url_for, request, make_response, redirect, session

from modes import SqlHelper
from . import index_blu


@index_blu.route('/qt')
def qt():
    session_username = session.get('username')
    if session_username:
        df = SqlHelper.Query(
            f"select UserNumber,UserName,UserPwd,Dept from UserManagement where UserNumber='{session_username}'")
        if df.shape[0] > 0:
            return render_template('index/qt.html', df=df)
        else:
            return redirect(url_for('.login'))
    return redirect(url_for('.login'))


@index_blu.route('/login')
def login():
    if request.args:
        user_Number = request.args.get('username')
        pwd = request.args.get('userpwd')
        df = SqlHelper.Query(
            f"select UserNumber,UserName,UserPwd,Dept from UserManagement where UserNumber='{user_Number}' and UserPwd='{pwd}'")
        if df.shape[0] > 0:
            response = make_response(redirect(url_for('.qt')))
            # response.set_cookie('username', user_Number, max_age=60)
            session['username'] = user_Number
            return response
        else:
            return render_template('index/login.html')
    return render_template('index/login.html')


@index_blu.route('/login_out')
def login_out():
    session.clear()
    return redirect(url_for('.qt'))
