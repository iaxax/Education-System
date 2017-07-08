#encoding:utf-8

from flask import Blueprint
from flask import render_template

page = Blueprint('page', __name__)

# 获取登录界面
@page.route('/', methods=['GET', 'POST'])
def getLoginHTML():
	return render_template('login.html')

# 获取退课界面
@page.route('/quitPage', methods=['GET', 'POST'])
def getQuitCourseHTML():
	return render_template('Drop.html')

# 获取选课界面
@page.route('/selectPage', methods=['GET', 'POST'])
def getSelectCourseHTML():
	return render_template('Choose.html')

# 获取主页面
@page.route('/home', methods=['GET', 'POST'])
def getHomeHTML():
	return render_template('index.html')

# 获取选课信息页面
@page.route('/showPage', methods=['GET', 'POST'])
def getCourseInfoHTML():
	return render_template('MyClass.html')

# 测试
@page.route('/test', methods=['GET', 'POST'])
def test():
	return render_template('/test.html')

#统计
@page.route('/statistic_stu', methods=['GET', 'POST'])
def getStatistic_stu():
	return render_template('/Statistics_student.html')

#统计
@page.route('/statistic_cou', methods=['GET', 'POST'])
def getStatistic_cou():
	return render_template('/Statistics_course.html')

#cross clss
@page.route('/cross', methods=['GET', 'POST'])
def getcross():
	return render_template('/cross-Class.html')

#cross class Choose
@page.route('/cross-choose', methods=['GET', 'POST'])
def crosschoose():
	return render_template('/cross-Class-choose.html')

#cross class Drop
@page.route('/cross-drop', methods=['GET', 'POST'])
def crossdrop():
	return render_template('/cross-Class-drop.html')
