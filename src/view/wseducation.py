# #encoding:utf-8

# from flask import Blueprint
# from flask import request
# from flask import session
# from src.view import isLogin

# wseducation = Blueprint('ieducation', __name__)

# # 获得课程统计信息
# @ieducation.route('/getCourseStatistics', methods=['GET', 'POST'])
# def igetCourseStatistics():
# 	return CourseService.igetCourseStatistics()

# # 获得学生统计信息
# @ieducation.route('/getStudentStatistics', methods=['GET', 'POST'])
# def igetStudentStatistics():
# 	return StudentService.igetStudentStatistics()

# # 根据ID列表获取相应课程信息
# @ieducation.route('/getCourseByIds', methods=['GET', 'POST'])
# def igetCourseByIds():
# 	idStr = request.form['courseIds']
# 	return CourseService.igetCourseInfoByIds(idStr.split(','))

# # 获取课程信息
# # 返回获取结果，提示信息和课程列表
# @ieducation.route('/getAllCourseInfo', methods=['GET', 'POST'])
# def igetAllCourseInfo():
# 	return CourseService.igetAllCourseInfo()

# # 获取学生的所选课程
# # 返回获取结果，提示信息和课程列表
# @ieducation.route('/getCourseInfo', methods=['GET', 'POST'])
# def igetCourseInfo():
# 	if (not isLogin()):
# 		return CourseService.getNotLoginResult()
	
# 	return CourseService.igetCourseInfo(session['username'])

# # 选课
# # 参数：课程ID
# # 返回选课结果和提示信息
# @ieducation.route('/selectCourse', methods=['POST'])
# def iselectCourse():
# 	if (not isLogin()):
# 		return CourseService.getNotLoginResult()
	
# 	courseId = request.form['courseId']
# 	username = session['username']
# 	courseDept = request.form['courseDept']
# 	return CourseService.iselectCourse(username, int(courseId), int(courseDept))
	
# # 退课
# # 参数：课程ID
# # 返回退课结果和提示信息
# @ieducation.route('/quitCourse', methods=['POST'])
# def iquitCourse():
# 	if (not isLogin()):
# 		return CourseService.getNotLoginResult()
	
# 	courseId = request.form['courseId']
# 	username = session['username']
# 	courseDept = request.form['courseDept']
# 	return CourseService.iquitCourse(username, int(courseId), int(courseDept))
