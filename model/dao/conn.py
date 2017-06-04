#encoding=utf-8

import sqlite3
import config

class Connection:
	__conn = None

	# 返回一个数据库连接实例
	@staticmethod
	def getConnection():
		if (not Connection.__conn):
			Connection.__conn = sqlite3.connect(config.db_path, check_same_thread=False)
				
		return Connection.__conn
				
	
