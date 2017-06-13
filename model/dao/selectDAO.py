#encoding=utf-8

from conn import Connection

class SelectDAO:

	# 获取学生选课数量
	@staticmethod
	def getSelectCourseNum(studentId):
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select count(*) from selection where student_id = %d"%(studentId)
		cursor.execute(sql)
		result = cursor.fetchone()
        return result[0]

	#获取课程选课学生数量
	def getSelectStudentNum(courseId):
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select count(*) from selection where course_id = %d"%(courseId)
		cursor.execute(sql)
		result = cursor.fetchone()
        return result[0]
