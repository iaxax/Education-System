#encoding:utf-8

from src.dao.accountDAO import AccountDAO
from src.util import xmlutil

"""
处理于账户有关的逻辑
"""
class AccountService:

	# 登录校验
	# 返回二元组(登录结果，提示信息)
	@staticmethod
	def login(username, password):
		if (AccountDAO.isAccountValid(username, password)):
			return {"success": unicode(True), "message": u"登录成功"}
		else:
			return {"success": unicode(False), "message": u"账号与密码不匹配"}
