from flask import render_template
from . import admin_blu

from modes import SqlHelper


@admin_blu.route('/index')
def index():
    df = SqlHelper.Query("select UserNumber,UserName,UserPwd,Dept from UserManagement")
    if df.shape[0] > 0:
        return render_template('admin/table.html', df=df)
    return render_template('admin/../../templates/index/login.html')
