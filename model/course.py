#coding:utf-8

from dao.courseDAO import CourseDAO
from dao.accountDAO import AccountDAO

class CourseService:

	# 将课程列表转换成字典
	@staticmethod
	def __toCourseDict(courses):
		result = [];
		for (id, name, addr, time, type, dept) in courses:
			result.append({
				'course_id': id, 'name':name,
				'classroom': addr, 'classtime': time,
				'type': type, 'department': dept
			})
		return result

	# 未登录而对课程相关内容进行请求时的返回信息
	@staticmethod
	def getNotLoginResult():
		return {'success':False, 'message':u'请先登录', 'courses':[]}
	
	# 获取所有的课程信息
	@staticmethod
	def getAllCourseInfo():
		info = CourseDAO.getAllCourseInfo()
		return {
			'success':True, 'message':u'获取课程信息成功',
			'courses':CourseService.__toCourseDict(info)
		}
		
	# 获取选课信息
	@staticmethod
	def getCourseInfo(username):
		id = AccountDAO.getStudentIdByUserName(username)
		info = CourseDAO.getCourseInfo(id)
		return {
			'success':True, 'message':u'获取选课信息成功',
			'courses':CourseService.__toCourseDict(info)
		}
	
	# 选课
	@staticmethod
	def selectCourse(username, courseId):
		id = AccountDAO.getStudentIdByUserName(username)
		result = CourseDAO.selectCourse(id, courseId)
		return {'success':result[0], 'message':result[1]}
	
	# 退课
	@staticmethod	
	def quitCourse(username, courseId):
		id = AccountDAO.getStudentIdByUserName(username)
		result = CourseDAO.quitCourse(id, courseId)
		return {'success':result[0], 'message':result[1]}
		
