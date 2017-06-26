#encoding:utf-8

from flask import Blueprint
from flask import request
from flask import session
from src.view import isLogin
from src.util import xmlutil
from src.service.normal.account import AccountService
from src.service.normal.course import CourseService
from src.service.normal.student import StudentService

education = Blueprint('education', __name__)

# 登录
# 设置会话中登录状态以及登录用户名称
# 返回登录结果和提示信息
@education.route('/login', methods=['POST'])
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
@education.route('/logout', methods=['POST'])
def logout():
	if (isLogin()):
		session['isLogin'] = True
		session['username'] = None

# 获取课程信息
# 返回获取结果，提示信息和课程列表
@education.route('/getAllCourseInfo', methods=['GET', 'POST'])
def getAllCourseInfo():
	return CourseService.getAllCourseInfo()

# 获取学生的所选课程
# 返回获取结果，提示信息和课程列表
@education.route('/getCourseInfo', methods=['GET', 'POST'])
def getCourseInfo():
	if (not isLogin()):
		return CourseService.getNotLoginResult()
	
	return CourseService.getCourseInfo(session['username'])
	
# 选课
# 参数：课程ID
# 返回选课结果和提示信息
@education.route('/selectCourse', methods=['POST'])
def selectCourse():
	if (not isLogin()):
		return CourseService.getNotLoginResult()
	
	courseId = request.form['courseId']
	username = session['username']
	return CourseService.selectCourse(username, int(courseId))
	
# 退课
# 参数：课程ID
# 返回退课结果和提示信息
@education.route('/quitCourse', methods=['POST'])
def quitCourse():
	if (not isLogin()):
		return CourseService.getNotLoginResult()
	
	courseId = request.form['courseId']
	username = session['username']
	return CourseService.quitCourse(username, int(courseId))

# 获得课程统计信息
@education.route('/getCourseStatistics', methods=['GET', 'POST'])
def getCourseStatistics():
	return CourseService.getCourseStatistics()
	
# 获得学生统计信息
@education.route('/getStudentStatistics', methods=['GET', 'POST'])
def getStudentStatistics():
	return StudentService.getStudentStatistics()