#coding:utf-8

from dao.studentDAO import StudentDAO
from dao.selectDAO import SelectDAO
from department import departmentId

class StudentService:

	# 根据学生ID获得该学生的选课数目
	def __getSelectCourseNum(studentId):
		return SelectDAO.getSelectCourseNum(studentId)

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
		return result

