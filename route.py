#coding:utf-8

from flask import Flask
from flask import request
from flask import session
from flask import render_template
from model.account import AccountService
from model.course import CourseService
from model.student import StudentService
from model import xmlutil

app = Flask(__name__)
app.secret_key = 'whatisasecretkey'

# 获取登录界面
@app.route('/', methods=['GET', 'POST'])
def getLoginHTML():
	return render_template('login.html')

# 获取退课界面
@app.route('/quitPage', methods=['GET', 'POST'])
def getQuitCourseHTML():
	return render_template('Drop.html')

# 获取选课界面
@app.route('/selectPage', methods=['GET', 'POST'])
def getSelectCourseHTML():
	return render_template('Choose.html')

# 获取主页面
@app.route('/home', methods=['GET', 'POST'])
def getHomeHTML():
	return render_template('index.html')

# 获取选课信息页面
@app.route('/showPage', methods=['GET', 'POST'])
def getCourseInfoHTML():
	return render_template('MyClass.html')

def isLogin():
	return 'isLogin' in session and session['isLogin']
	
# 测试
@app.route('/test', methods=['GET', 'POST'])
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
		
	return xmlutil.loginResultToXml(loginResult)

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
@app.route('/getAllCourseInfo', methods=['GET', 'POST'])
def getAllCourseInfo():
	return xmlutil.courseResultToXml(CourseService.getAllCourseInfo())


# 获取学生的所选课程
# 返回获取结果，提示信息和课程列表
@app.route('/getCourseInfo', methods=['GET', 'POST'])
def getCourseInfo():
	if (not isLogin()):
		return xmlutil.loginResultToXml(CourseService.getNotLoginResult())
	
	return xmlutil.courseResultToXml(CourseService.getCourseInfo(session['username']))

	
# 选课
# 参数：课程ID
# 返回选课结果和提示信息
@app.route('/selectCourse', methods=['POST'])
def selectCourse():
	if (not isLogin()):
		return xmlutil.loginResultToXml(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	return xmlutil.loginResultToXml(CourseService.selectCourse(username, int(courseId)))
	
	
# 退课
# 参数：课程ID
# 返回退课结果和提示信息
@app.route('/quitCourse', methods=['POST'])
def quitCourse():
	if (not isLogin()):
		return xmlutil.loginResultToXml(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	return xmlutil.loginResultToXml(CourseService.quitCourse(username, int(courseId)))

# 获得课程统计信息
@app.route('/getCourseStatistics', methods=['GET', 'POST'])
def getCourseStatistics():
	result = CourseService.getCourseStatistics()
	return xmlutil.icourseStatisticsToXml(result)
	
# 获得学生统计信息
@app.route('/getStudentStatistics', methods=['GET', 'POST'])
def getStudentStatistics():
	result = StudentService.getStudentStatistics()
	return xmlutil.istudentStatisticsToXml(result)

# -----------------------------数据集成之前的接口(END)--------------------------------

# -----------------------------数据集成之后的接口(BEGIN)------------------------------

# 根据ID列表获取相应课程信息
@app.route('/igetCourseByIds', methods=['GET', 'POST'])
def igetCourseByIds():
	idStr = request.form['courseIds']
	return xmlutil.icourseResultToXml(CourseService.igetCourseInfoByIds(idStr.split(',')))


# 获取课程信息
# 返回获取结果，提示信息和课程列表
@app.route('/igetAllCourseInfo', methods=['GET', 'POST'])
def igetAllCourseInfo():
	return xmlutil.icourseResultToXml(CourseService.igetAllCourseInfo())


# 获取学生的所选课程
# 返回获取结果，提示信息和课程列表
@app.route('/igetCourseInfo', methods=['GET', 'POST'])
def igetCourseInfo():
	if (not isLogin()):
		return xmlutil.loginResultToXml(CourseService.getNotLoginResult())
	
	return xmlutil.icourseResultToXml(CourseService.igetCourseInfo(session['username']))

	
# 选课
# 参数：课程ID
# 返回选课结果和提示信息
@app.route('/iselectCourse', methods=['POST'])
def iselectCourse():
	if (not isLogin()):
		return xmlutil.loginResultToXml(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	courdeDept = request.form['courseDept']
	return xmlutil.loginResultToXml(CourseService.iselectCourse(username, int(courseId), int(courseDept)))
	
	
# 退课
# 参数：课程ID
# 返回退课结果和提示信息
@app.route('/iquitCourse', methods=['POST'])
def iquitCourse():
	if (not isLogin()):
		return xmlutil.loginResultToXml(CourseService.getNotLoginResult())
	
	courseId = request.form['courseId']
	username = session['username']
	courseDept = request.form['courseDept']
	return xmlutil.icourseResultToXml(CourseService.iquitCourse(username, int(courseId), int(courseDept)))

# ------------------------------数据集成之后的接口(END)--------------------------------


if __name__ == '__main__':
    app.run(host='0.0.0.0')
