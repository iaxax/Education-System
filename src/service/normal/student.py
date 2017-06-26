#coding:utf-8

from src.dao.studentDAO import StudentDAO
from src.dao.selectDAO import SelectDAO
from src.service.department import departmentId
from src.service.netstudent import NetStudent
import src.util.xmlutil

class StudentService:

	# 根据学生ID获得该学生的选课数目
	@staticmethod
	def __getSelectCourseNum(studentId):
		return SelectDAO.getSelectCourseNum(studentId)

	# 获取所有学生统计信息
	@staticmethod
	def igetStudentStatistics():
		return xmlutil.istudentStatisticsToXml(NetStudent.getAllStudentStatInfo())

	# 获取学生统计信息
	@staticmethod
	def getStudentStatistics():
		allInfo = StudentDAO.getAllStudentInfo()
		result = []
		for info in allInfo:
			num = StudentService.__getSelectCourseNum(info[0])
			result.append({
				"studentId": unicode(info[0]), "courseNum":unicode(num), "name": info[1],
				"institutionId": unicode(departmentId)
			})
		return xmlutil.istudentStatisticsToXml(result)

