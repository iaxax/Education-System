#encoding:utf-8

from flask import Blueprint
from flask import request
from flask import session
from src.view import isLogin
from src.service.webservice.wscourse import CourseWebService
from src.service.webservice.wsstudent import StudentWebService

wseducation = Blueprint('wseducation', __name__)

# 获得课程统计信息
@wseducation.route('/getCourseStatistics', methods=['GET', 'POST'])
def wsGetCourseStatistics():
	return CourseWebService.wsGetCourseStatInfo()

# 获得学生统计信息
@wseducation.route('/getStudentStatistics', methods=['GET', 'POST'])
def wsGetStudentStatistics():
	return StudentWebService.wsGetStudentStatInfo()

# 获取课程信息
@wseducation.route('/getAllCourseInfo', methods=['GET', 'POST'])
def wsGetAllCourseInfo():
	return CourseWebService.wsGetAllCourseInfo()

# 获取学生的所选课程
@wseducation.route('/getCourseInfo', methods=['GET', 'POST'])
def wsGetCourseInfo():
	if (not isLogin()):
		return CourseWebService.wsGetNotLoginResult()
	
	return CourseWebService.wsGetSelectCourseInfo(session['username'])

# 选课
# 参数：课程ID
# 返回选课结果和提示信息
@wseducation.route('/selectCourse', methods=['POST'])
def wsSelectCourse():
	if (not isLogin()):
		return CourseWebService.wsGetNotLoginResult()
	
	courseId = request.form['courseId']
	username = session['username']
	courseDept = request.form['courseDept']
	return CourseWebService.wsSelectCourse(username, int(courseId), int(courseDept))
	
# 退课
# 参数：课程ID
# 返回退课结果和提示信息
@wseducation.route('/quitCourse', methods=['POST'])
def wsQuitCourse():
	if (not isLogin()):
		return CourseWebService.wsGetNotLoginResult()
	
	courseId = request.form['courseId']
	username = session['username']
	courseDept = request.form['courseDept']
	return CourseWebService.wsQuitCourse(username, int(courseId), int(courseDept))
