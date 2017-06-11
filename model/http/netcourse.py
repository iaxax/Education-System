#encoding:utf-8

from netutil import get
from netutil import post
from netcfg import allCourseUrl
from netcfg import selectCourseUrl
from netcfg import selectUrl
from netcfg import quitUrl
from xmlutil import xmlToCourseInfo
from xmlutil import xmlToResultInfo

class NetCourse:

    # 从其他院系请求课程信息
    @staticmethod
    def getAllCourseInfo(departmentId):
        data = {'institution': departmentId}
        allCourseXml = post(allCourseUrl, data)
        return xmlToCourseInfo(allCourseXml)

    # 从其他院系请求选课信息
    @staticmethod
    def getSelectCourseInfo(studentId, studentDept):
        data = {'studentid': studentId, 'studentInstitution': studentDept}
        selectCourseXml = post(selectCourseUrl, data)
        return xmlToCourseInfo(selectCourseXml)

    # 从其他院系选课
    @staticmethod
    def selectCourse(studentId, studentDept, courseId, courseDept):
        data = {
                'studentid': studentId, 'studentInstitution': studentDept,
                'courseid': courseId, 'courseInstitution': courseDept
        }
        selectResultXml = post(selectUrl, data)
        return xmlToResultInfo(selectResultXml)

    # 从其他院系退课
    @staticmethod
    def quitCourse(studentId, studentDept, courseId, courseDept):
        data = {
            'studentid': studentId, 'studentInstitution': studentDept,
            'coureseid': courseId, 'courseInstitution': courseDept
        }
        quitResultXml = post(quitUrl, data)
        return xmlToResultInfo(quitResultXml)
        
