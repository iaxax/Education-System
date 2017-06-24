#encoding:utf-8

from conn import Connection

class AccountDAO:

	# 判断一个账户是否有效
	# 返回boolean
	@staticmethod
	def isAccountValid(username, password):
		connection = Connection.getConnection()
		cursor = connection.cursor()	
		sql = "select * from student_account where username = '%s' and password = '%s'"%(username, password)
		cursor.execute(sql)
		resultList = cursor.fetchall()
		
		return len(resultList) == 1

	# 根据登录名获取学号
	# 返回学号
	@staticmethod
	def getStudentIdByUserName(username):
		conn = Connection.getConnection()
		cursor = conn.cursor()
		sql = "select student_id from student_account where username = '%s'"%(username)
		cursor.execute(sql)
		
		return cursor.fetchone()[0]
	