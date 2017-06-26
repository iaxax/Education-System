#encoding:utf-8

from flask import Blueprint
from flask import request
from flask import session
from src.view import isLogin
from src.service.integration.netcourse import NetCourse
from src.service.integration.netstudent import NetStudent

ieducation = Blueprint('ieducation', __name__)

# 获得课程统计信息
@ieducation.route('/getCourseStatistics', methods=['GET', 'POST'])
def iGetCourseStatistics():
	return NetCourse.iGetCourseStatInfo()

# 获得学生统计信息
@ieducation.route('/getStudentStatistics', methods=['GET', 'POST'])
def iGetStudentStatistics():
	return NetStudent.iGetStudentStatInfo()

# 根据ID列表获取相应课程信息
@ieducation.route('/getCourseByIds', methods=['GET', 'POST'])
def iGetCourseByIds():
	idStr = request.form['courseIds']
	return NetCourse.iGetCourseInfoByIds(idStr.split(','))

# 获取所有课程信息
@ieducation.route('/getAllCourseInfo', methods=['GET', 'POST'])
def iGetAllCourseInfo():
	return NetCourse.iGetAllCourseInfo()

# 获取学生的所选课程
@ieducation.route('/getCourseInfo', methods=['GET', 'POST'])
def iGetCourseInfo():
	if (not isLogin()):
		return NetCourse.iGetNotLoginResult()
	
	return NetCourse.iGetSelectCourseInfo(session['username'])

# 选课
# 参数：课程ID
# 返回选课结果和提示信息
@ieducation.route('/selectCourse', methods=['POST'])
def iSelectCourse():
	if (not isLogin()):
		return NetCourse.iGetNotLoginResult()
	
	courseId = request.form['courseId']
	username = session['username']
	courseDept = request.form['courseDept']
	return NetCourse.iSelectCourse(username, int(courseId), int(courseDept))
	
# 退课
# 参数：课程ID
# 返回退课结果和提示信息
@ieducation.route('/quitCourse', methods=['POST'])
def iQuitCourse():
	if (not isLogin()):
		return NetCourse.iGetNotLoginResult()
	
	courseId = request.form['courseId']
	username = session['username']
	courseDept = request.form['courseDept']
	return NetCourse.iQuitCourse(username, int(courseId), int(courseDept))
