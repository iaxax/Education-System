#encoding:utf-8

from dao.accountDAO import AccountDAO

class AccountService:

	# 登录校验
	# 返回二元组(登录结果，提示信息)
	@staticmethod
	def login(username, password):
		if (AccountDAO.isAccountValid(username, password)):
			return {"success": '1', "message": u"登录成功"}
		else:
			return {"success": '0', "message": u"账号与密码不匹配"}
