#coding:utf-8

from dao.courseDAO import CourseDAO
from dao.accountDAO import AccountDAO
from http import netcourse

class CourseService:

	# 院系ID
	__DEPARTMENT_ID = 2

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
		return {'success': '0', 'message':u'请先登录', 'courses':[]}
	
	# 获取所有的课程信息
	@staticmethod
	def getAllCourseInfo():
		return {
			'success': '1', 'message':u'获取课程信息成功',
			'courses': CourseService.__toCourseDict(CourseDAO.getAllCourseInfo())
		}
		
	# 获取选课信息
	@staticmethod
	def getCourseInfo(username):
		id = AccountDAO.getStudentIdByUserName(username)
		return {
			'success': '1', 'message':u'获取选课信息成功',
			'courses': CourseService.__toCourseDict(CourseDAO.getCourseInfo(id))
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
		
	# ------------------------------数据集成之后的处理逻辑(BEGIN)------------------------------------

	# 将课程列表转换成字典
	@staticmethod
	def __itoCourseDict(courses):
		newCourses = map(lambda x : (__DEPARTMENT_ID,) + x , courses)
		result = []

		for (deptId, id, name, addr, time, classtype, dept) in newCourses:
			result.append({
				"department_id": unicode(deptId),
				'course_id': unicode(id), 'name':name,
				'classroom': addr, 'classtime': time,
				'type': classtype, 'department': dept
			})
		return result

	# 根据ID列表获取相应课程
	@staticmethod
	def igetCourseInfoByIds(ids):
		courseList = []
		for id in ids:
			courseList.extend(CourseDAO.getCourseInfoById(int(id)))
		return {
			'success': '1', 'message':u'获取课程信息成功',
			'courses': CourseService.__itoCourseDict(courseList)
		}

	# 获取所有的课程信息
	@staticmethod
	def igetAllCourseInfo():
		info = CourseDAO.getAllCourseInfo()
		otherInfo = netcourse.getAllCourseInfo(__DEPARTMENT_ID)
		info.extend(otherInfo)

		return {
			'success': '1', 'message':u'获取课程信息成功',
			'courses': CourseService.__itoCourseDict(info)
		}
		
	# 获取选课信息
	@staticmethod
	def igetCourseInfo(username):
		id = AccountDAO.getStudentIdByUserName(username)
		info = CourseDAO.getCourseInfo(id)
		otherInfo = netcourse.getSelectCourseInfo(id, __DEPARTMENT_ID)
		info.extend(otherInfo)

		return {
			'success': '1', 'message':u'获取选课信息成功',
			'courses': CourseService.__itoCourseDict(info)
		}
	
	# 选课
	@staticmethod
	def iselectCourse(username, courseId, courseDept):
		result = None
		id = AccountDAO.getStudentIdByUserName(username)

		if (courseDept == CourseService.__DEPARTMENT_ID):
			result = CourseDAO.selectCourse(id, courseId)
		else:
			result = netcourse.selectCourse(id, CourseService.__DEPARTMENT_ID, courseId, courseDept)

		return {'success':result[0], 'message':result[1]}
	
	# 退课
	@staticmethod	
	def iquitCourse(username, courseId, courseDept):
		result = None
		id = AccountDAO.getStudentIdByUserName(username)

		if (courseDept == CourseService.__DEPARTMENT_ID):
			result = CourseDAO.quitCourse(id, courseId)
		else:
			result = netcourse.selectCourse(id, CourseService.__DEPARTMENT_ID, courseId, courseDept)
			
		return {'success': result[0], 'message':result[1]}

	# ------------------------------数据集成之后的处理逻辑(END)---------------------------------------
