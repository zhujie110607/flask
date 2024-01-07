from flask import Flask
from views.admin import admin_blu
from views.index import index_blu

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'  # 用于加密cookie

app.register_blueprint(admin_blu, url_prefix='/admin')  # 注册蓝图 url_prefix='/admin' 为蓝图的访问路径
app.register_blueprint(index_blu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
