#encoding=utf-8

import pymssql
import config

class Connection:
	__conn = None

	# 返回一个数据库连接实例
	@staticmethod
	def getConnection():
		if (not Connection.__conn):
			Connection.__conn = pymssql.connect( \
				host=config.host, \
				user=config.username, \
				password=config.password, \
				database=config.dbName, \
				charset='utf8')
				
		return Connection.__conn
				
	