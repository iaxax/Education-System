#encoding:utf-8

from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

__xml = '<?xml version="1.0" encoding="utf-8"?>'

def courseResultToXml(result):
    root = Element('result')
    success = SubElement(root, 'success')
    success.text = result['success']
    message = SubElement(root, 'message')
    message.text = result['message']
    courses = SubElement(root, 'courses')

    for c in result['courses']:
        course = SubElement(courses, 'course')
        courseId = SubElement(course, 'course_id')
        courseId.text = c['course_id']
        name = SubElement(course, 'name')
        name.text = c['name']
        classroom = SubElement(course, 'classroom')
        classroom.text = c['classroom']
        classtime = SubElement(course, 'classtime')
        classtime.text = c['classtime']
        classtype = SubElement(course, 'type')
        classtype.text = c['type']
        department = SubElement(course, 'department')
        department.text = c['department']

    return __xml + ET.tostring(root, encoding='utf-8', method='xml')

def icourseResultToXml(result):
    root = Element('result')
    success = SubElement(root, 'success')
    success.text = result['success']
    message = SubElement(root, 'message')
    message.text = result['message']
    courses = SubElement(root, 'courses')

    for c in result['courses']:
        course = SubElement(courses, 'course')
        courseId = SubElement(course, 'course_id')
        courseId.text = c['course_id']
        name = SubElement(course, 'name')
        name.text = c['name']
        classroom = SubElement(course, 'classroom')
        classroom.text = c['classroom']
        classtime = SubElement(course, 'classtime')
        classtime.text = c['classtime']
        classtype = SubElement(course, 'type')
        classtype.text = c['type']
        department = SubElement(course, 'department')
        department.text = c['department']
        departmentId = SubElement(course, 'department_id')
        departmentId.text = c['department_id']

    return __xml + ET.tostring(root, encoding='utf-8', method='xml')

def loginResultToXml(result):
    root = Element('result')
    success = SubElement(root, 'success')
    success.text = result['success']
    message = SubElement(root, 'message')
    message.text = result['message']
    return __xml + ET.tostring(root, encoding='utf-8', method='xml')