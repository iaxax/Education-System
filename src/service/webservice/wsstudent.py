#encoding:utf-8

from src.util.wsutil import client

class StudentWebService:

    @staticmethod
    def wsGetStudentStatInfo():
        return client.service.getStudentStatistics()