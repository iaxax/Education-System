#coding:utf-8

from flask import Flask
from src.view.page import page
from src.view.education import education
from src.view.ieducation import ieducation
# from src.view.wseducation import wseducation

app = Flask(__name__)
app.secret_key = 'whatisasecretkey'

# 注册静态页面相关的访问路径
app.register_blueprint(page, url_prefix='/page')
# 注册本地信息的访问路径
app.register_blueprint(education, url_prefix='/education')
# 注册集成信息的访问路径
app.register_blueprint(ieducation, url_prefix='/education/integration')
# 注册通过Web Service集成信息的访问路径
# app.register_blueprint(wseducation, url_prefix='/education/webservice')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
