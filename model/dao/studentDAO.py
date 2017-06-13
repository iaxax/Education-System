#encoding=utf-8

from conn import Connection

class StudentDAO:
	# 获取学生信息
	@staticmethod
	def getAllStudentInfo():
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		return cursor.fetchall()