#encoding:utf-8

import sys
sys.path.append('..')

from src.util.netutil import get
from src.util.netutil import post
from src.service import departmentId
from src.config.netcfg import allCourseUrl
from src.config.netcfg import selectCourseUrl
from src.config.netcfg import selectUrl
from src.config.netcfg import quitUrl
from src.config.netcfg import courseStatUrl
from src.util import xmlutil
from src.dao.accountDAO import AccountDAO
from src.dao.courseDAO import CourseDAO

"""
获取与课程信息相关的集成信息
"""
class NetCourse:

    # 根据ID列表获取相应课程
	@staticmethod
	def iGetCourseInfoByIds(ids):
		courseList = []
		for id in ids:
			courseList.extend(CourseDAO.getCourseInfoById(int(id)))
		return xmlutil.icourseResultToXml({
			'success': unicode(True), 'message':u'获取课程信息成功',
			'courses': NetCourse.__itoCourseDict(courseList)
		})

	# 获取所有的课程信息
	@staticmethod
	def iGetAllCourseInfo():
		info = CourseDAO.getAllCourseInfo()
		info = map(lambda x : (departmentId,) + x , info)
		otherInfo = NetCourse.__iGetOtherCourseInfo(departmentId)
		info.extend(otherInfo)

		return xmlutil.icourseResultToXml({
			'success': unicode(True), 'message':u'获取课程信息成功',
			'courses': NetCourse.__itoCourseDict(info)
		})
		
	# 获取选课信息
	@staticmethod
	def iGetSelectCourseInfo(username):
		id = AccountDAO.getStudentIdByUserName(username)
		info = CourseDAO.getCourseInfo(id)
		info = map(lambda x : (departmentId,) + x , info)
		otherInfo = NetCourse.__iGetOtherSelectCourseInfo(id, departmentId)
		info.extend(otherInfo)

		return xmlutil.icourseResultToXml({
			'success': unicode(True), 'message':u'获取选课信息成功',
			'courses': NetCourse.__itoCourseDict(info)
		})
	
	# 选课
	@staticmethod
	def iSelectCourse(username, courseId, courseDept):
		result = None
		id = AccountDAO.getStudentIdByUserName(username)

		if (courseDept == departmentId):
			result = CourseDAO.selectCourse(id, courseId)
		else:
			result = NetCourse.__iSelectCourse(id, departmentId, courseId, courseDept)

		return xmlutil.loginResultToXml({
			'success': unicode(result[0]), 'message': unicode(result[1])
		})
	
	# 退课
	@staticmethod	
	def iQuitCourse(username, courseId, courseDept):
		result = None
		id = AccountDAO.getStudentIdByUserName(username)

		if (courseDept == departmentId):
			result = CourseDAO.quitCourse(id, courseId)
		else:
			result = NetCourse.__iQuitCourse(id, departmentId, courseId, courseDept)
			
		return xmlutil.loginResultToXml({
			'success': unicode(result[0]), 'message':unicode(result[1])
		})

    # 获得所有的课程统计信息
	@staticmethod
	def iGetCourseStatInfo():
		return get(courseStatUrl)

	# 获得没有登录时的提示信息
	@staticmethod
	def iGetNotLoginResult():
		return xmlutil.loginResultToXml({'success': unicode(False), 'message':u'请先登录', 'courses':[]})

    # 从其他院系请求课程信息
	@staticmethod
	def __iGetOtherCourseInfo(departmentId):
		data = {'institutionId': departmentId}
		allCourseXml = post(allCourseUrl, data)
		print '------------------------------'
		print allCourseXml
		print '------------------------------'
		return xmlutil.xmlToCourseInfo(allCourseXml)

    # 从其他院系请求选课信息
	@staticmethod
	def __iGetOtherSelectCourseInfo(studentId, studentDept):
		data = {'studentId': studentId, 'institutionId': studentDept}
		selectCourseXml = post(selectCourseUrl, data)
		return xmlutil.xmlToCourseInfo(selectCourseXml)

    # 从其他院系选课
	@staticmethod
	def __iSelectCourse(studentId, studentDept, courseId, courseDept):
		data = {
                'studentId': studentId, 'studentInstitution': studentDept,
                'courseId': courseId, 'courseInstitution': courseDept
        }
		selectResultXml = post(selectUrl, data)
		return xmlutil.xmlToResultInfo(selectResultXml)

    # 从其他院系退课
	@staticmethod
	def __iQuitCourse(studentId, studentDept, courseId, courseDept):
		data = {
            'studentId': studentId, 'studentInstitution': studentDept,
            'coureseId': courseId, 'courseInstitution': courseDept
        }
		quitResultXml = post(quitUrl, data)
		return xmlutil.xmlToResultInfo(quitResultXml)
        
    # 根据课程ID获得选择该课程的人数
	@staticmethod
	def __getSelectStudentNum(courseId):
		return SelectDAO.getSelectStudentNum(courseId)

	# 将课程列表转换成字典
	@staticmethod
	def __itoCourseDict(courses):
		result = []
		for (deptId, id, name, addr, time, classtype, dept) in courses:
			result.append({
				"department_id": unicode(deptId),
				'course_id': unicode(id), 'name':name,
				'classroom': addr, 'classtime': time,
				'type': classtype, 'department': dept
			})
		return result

