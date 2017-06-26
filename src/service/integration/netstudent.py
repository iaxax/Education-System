#encoding:utf-8

from src.util.netutil import get
from src.config.netcfg import studentStatUrl

"""
获取于学生信息相关的集成信息
"""
class NetStudent:

    # 获取全部的学生统计信息
    @staticmethod
    def iGetStudentStatInfo():
        return get(studentStatUrl)
