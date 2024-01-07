from flask import Blueprint

admin_blu = Blueprint('admin', __name__)  # 注册蓝图

from . import views
