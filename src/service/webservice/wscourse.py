#encoding:utf-8

from src.service import departmentId
from src.util import xmlutil
from src.util.wsutil import client
from src.dao.accountDAO import AccountDAO
from src.dao.courseDAO import CourseDAO

"""
通过Web Service 获得与课程信息有关的远程信息
"""
class CourseWebService:

	# 获取所有的课程信息
	@staticmethod
	def wsGetAllCourseInfo():
		info = CourseDAO.getAllCourseInfo()
		info = map(lambda x : (departmentId,) + x , info)
		otherInfo = CourseWebService.__wsGetOtherCourseInfo(departmentId)
		info.extend(otherInfo)

		return xmlutil.icourseResultToXml({
			'success': unicode(True), 'message':u'获取课程信息成功',
			'courses': CourseWebService.__wsToCourseDict(info)
		})
		
	# 获取选课信息
	@staticmethod
	def wsGetSelectCourseInfo(username):
		id = AccountDAO.getStudentIdByUserName(username)
		info = CourseDAO.getCourseInfo(id)
		info = map(lambda x : (departmentId,) + x , info)
		otherInfo = CourseWebService.__wsGetOtherSelectCourseInfo(id, departmentId)
		info.extend(otherInfo)

		return xmlutil.icourseResultToXml({
			'success': unicode(True), 'message':u'获取选课信息成功',
			'courses': CourseWebService.__wsToCourseDict(info)
		})
	
	# 选课
	@staticmethod
	def wsSelectCourse(username, courseId, courseDept):
		result = None
		id = AccountDAO.getStudentIdByUserName(username)

		if (courseDept == departmentId):
			result = CourseDAO.selectCourse(id, courseId)
		else:
			result = CourseWebService.__wsSelectCourse(id, departmentId, courseId, courseDept)

		return xmlutil.loginResultToXml({
			'success': unicode(result[0]), 'message': unicode(result[1])
		})
	
	# 退课
	@staticmethod	
	def wsQuitCourse(username, courseId, courseDept):
		result = None
		id = AccountDAO.getStudentIdByUserName(username)

		if (courseDept == departmentId):
			result = CourseDAO.quitCourse(id, courseId)
		else:
			result = CourseWebService.__wsQuitCourse(id, departmentId, courseId, courseDept)
			
		return xmlutil.loginResultToXml({
			'success': unicode(result[0]), 'message':unicode(result[1])
		})

    # 获得所有的课程统计信息
	@staticmethod
	def wsGetCourseStatInfo():
		return client.service.getCourseStatistics()

	# 获得没有登录时的提示信息
	@staticmethod
	def wsGetNotLoginResult():
		return xmlutil.loginResultToXml({'success': unicode(False), 'message':u'请先登录', 'courses':[]})

    # 从其他院系请求课程信息
	@staticmethod
	def __wsGetOtherCourseInfo(departmentId):
		infoXml = client.service.getAllCourses(departmentId)
		return xmlutil.xmlToCourseInfo(infoXml)

    # 从其他院系请求选课信息
	@staticmethod
	def __wsGetOtherSelectCourseInfo(studentId, studentDept):
		infoXml = client.service.getStudyCourses(studentDept, studentId)
		return xmlutil.xmlToCourseInfo(infoXml)

    # 从其他院系选课
	@staticmethod
	def __wsSelectCourse(studentId, studentDept, courseId, courseDept):
		infoXml = client.service.chooseCourses(studentDept, studentId, courseDept, courseId)
		return xmlutil.xmlToResultInfo(infoXml)

    # 从其他院系退课
	@staticmethod
	def __wsQuitCourse(studentId, studentDept, courseId, courseDept):
		infoXml = client.service.dropCourses(studentDept, studentId, courseDept, courseId)
		return xmlutil.xmlToResultInfo(infoXml)
        
    # 根据课程ID获得选择该课程的人数
	@staticmethod
	def __getSelectStudentNum(courseId):
		return SelectDAO.getSelectStudentNum(courseId)

	# 将课程列表转换成字典
	@staticmethod
	def __wsToCourseDict(courses):
		result = []
		for (deptId, id, name, addr, time, classtype, dept) in courses:
			result.append({
				"department_id": unicode(deptId),
				'course_id': unicode(id), 'name':name,
				'classroom': addr, 'classtime': time,
				'type': classtype, 'department': dept
			})
		return result


    