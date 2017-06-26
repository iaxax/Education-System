#coding:utf-8

from src.dao.courseDAO import CourseDAO
from src.dao.accountDAO import AccountDAO
from src.dao.selectDAO import SelectDAO
from src.service import departmentId
from src.util import xmlutil

"""
处理于课程信息有关的本地信息
"""
class CourseService:

	# 将课程列表转换成字典
	@staticmethod
	def __toCourseDict(courses):
		result = []
		for (id, name, addr, time, classtype, dept) in courses:
			result.append({
				'course_id': unicode(id), 'name':name,
				'classroom': addr, 'classtime': time,
				'type': classtype, 'department': dept
			})
		return result

	# 未登录而对课程相关内容进行请求时的返回信息
	@staticmethod
	def getNotLoginResult():
		return xmlutil.loginResultToXml({'success': unicode(False), 'message':u'请先登录', 'courses':[]})
	
	# 获取所有的课程信息
	@staticmethod
	def getAllCourseInfo():
		return xmlutil.courseResultToXml({
			'success': unicode(True), 'message':u'获取课程信息成功',
			'courses': CourseService.__toCourseDict(CourseDAO.getAllCourseInfo())
		})
		
	# 获取选课信息
	@staticmethod
	def getCourseInfo(username):
		id = AccountDAO.getStudentIdByUserName(username)
		return xmlutil.courseResultToXml({
			'success': unicode(True), 'message':u'获取选课信息成功',
			'courses': CourseService.__toCourseDict(CourseDAO.getCourseInfo(id))
		})
	
	# 选课
	@staticmethod
	def selectCourse(username, courseId):
		id = AccountDAO.getStudentIdByUserName(username)
		result = CourseDAO.selectCourse(id, courseId)
		return xmlutil.loginResultToXml({'success':result[0], 'message':result[1]})
	
	# 退课
	@staticmethod	
	def quitCourse(username, courseId):
		id = AccountDAO.getStudentIdByUserName(username)
		result = CourseDAO.quitCourse(id, courseId)
		return xmlutil.loginResultToXml({'success':result[0], 'message':result[1]})

	# 获取课程统计信息
	@staticmethod
	def getCourseStatistics():
		allInfo = CourseDAO.getAllCourseInfo()
		result = []
		for info in allInfo:
			num = CourseService.__getSelectStudentNum(info[0])
			result.append({
				"courseId": unicode(info[0]), "studentNum": unicode(num), "name": info[1],
				 "institutionId": unicode(departmentId)
			})
		return xmlutil.icourseStatisticsToXml(result)

