#encoding:utf-8

from flask import session

def isLogin():
	return 'isLogin' in session and session['isLogin']