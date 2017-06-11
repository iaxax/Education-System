#coding:utf-8

from flask import Flask
from flask import request
from flask import session
from flask import render_template
from model.account import AccountService
from model.course import CourseService
import json

app = Flask(__name__)
app.secret_key = 'whatisasecretkey'

# 获取登录界面
@app.route('/', methods=['GET'])
def getLoginHTML():
	return render_template('login.html')

# 获取退课界面
@app.route('/quitPage', methods=['GET'])
def getQuitCourseHTML():
	return render_template('Drop.html')

# 获取选课界面
@app.route('/selectPage', methods=['GET'])
def getSelectCourseHTML():
	return render_template('Choose.html')

# 获取主页面
@app.route('/home', methods=['GET'])
def getHomeHTML():
	return render_template('index.html')

# 获取选课信息页面
@app.route('/showPage', methods=['GET'])
def getCourseInfoHTML():
	return render_template('MyClass.html')

def isLogin():
	return 'isLogin' in session and session['isLogin']
	
# 测试
@app.route('/test', methods=['GET'])
def test():
	return render_template('/test.html')

# 登录
# 设置会话中登录状态以及登录用户名称
# 返回登录结果和提示信息
@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	loginResult = AccountService.login(username, password)
	
	if (loginResult['success']):
		session['isLogin'] = True
		session['username'] = username
	else:
		session['isLogin'] = False
		session['username'] = None
		
	return json.dumps(loginResult, ensure_ascii=False)

# 登出
# 设置会话相关属性
# 无返回值
@app.route('/logout', methods=['POST'])
def logout():
	if (isLogin()):
		session['isLogin'] = True
		session['username'] = None


# --------------------------数据集成之前的接口(BEGIN)--------------------------------

# 获取课程信息
# 返回获取结果，提示信息和课程列表
@app.route('/getAllCourseInfo', methods=['GET'])
def getAllCourseInfo():
	return json.dumps(CourseService.getAllCourseInfo(), ensure_ascii=False)


# 获取学生的所选课程
# 返回获取结果，提示信息和课程列表
@app.route('/getCourseInfo', methods=['GET'])
def getCourseInfo():
	if (not isLogin()):
		return json.dumps(CourseService.getNotLoginResult())
	
	return json.dumps(CourseService.getCourseInfo(session['username']), ensure_ascii=False)

	
# 选课
# 参数：课程ID
# 返回选课结果和提示信息
@app.route('/selectCourse', methods=['POST'])
def selectCourse():
	if (not isLogin()):
		return json.dumps(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	return json.dumps(CourseService.selectCourse(username, int(courseId)), ensure_ascii=False)
	
	
# 退课
# 参数：课程ID
# 返回退课结果和提示信息
@app.route('/quitCourse', methods=['POST'])
def quitCourse():
	if (not isLogin()):
		return json.dumps(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	return json.dumps(CourseService.quitCourse(username, int(courseId)), ensure_ascii=False)

# -----------------------------数据集成之前的接口(END)--------------------------------

# -----------------------------数据集成之后的接口(BEGIN)------------------------------

# 获取课程信息
# 返回获取结果，提示信息和课程列表
@app.route('/igetAllCourseInfo', methods=['GET'])
def igetAllCourseInfo():
	return json.dumps(CourseService.igetAllCourseInfo(), ensure_ascii=False)


# 获取学生的所选课程
# 返回获取结果，提示信息和课程列表
@app.route('/igetCourseInfo', methods=['GET'])
def igetCourseInfo():
	if (not isLogin()):
		return json.dumps(CourseService.getNotLoginResult())
	
	return json.dumps(CourseService.igetCourseInfo(session['username']), ensure_ascii=False)

	
# 选课
# 参数：课程ID
# 返回选课结果和提示信息
@app.route('/iselectCourse', methods=['POST'])
def iselectCourse():
	if (not isLogin()):
		return json.dumps(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	courdeDept = request.form['courseDept']
	return json.dumps(CourseService.iselectCourse(username, int(courseId), int(courseDept)), ensure_ascii=False)
	
	
# 退课
# 参数：课程ID
# 返回退课结果和提示信息
@app.route('/iquitCourse', methods=['POST'])
def iquitCourse():
	if (not isLogin()):
		return json.dumps(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	courseDept = request.form['courseDept']
	return json.dumps(CourseService.iquitCourse(username, int(courseId), int(courseDept)), ensure_ascii=False)

# ------------------------------数据集成之后的接口(END)--------------------------------


if __name__ == '__main__':
    app.run(host='0.0.0.0')
