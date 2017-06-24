#encoding:utf-8

from src.util.netutil import get
from src.config.netcfg import studentStatUrl

class NetStudent:

    # 获取全部的学生统计信息
    @staticmethod
    def getAllStudentStatInfo():
        return get(studentStatUrl)
