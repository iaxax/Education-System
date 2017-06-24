#encoding:utf-8

from conn import Connection
import numpy as np
import random

# 随机生成电话号码
def createPhoneNum():
	return random.choice(['182', '157', '136']) + "".join(random.choice("0123456789") for i in range(8))

# 随机生成姓名
first_name = [u'赵', u'钱', u'孙', u'李', u'吴', u'王', u'陈', u'林']
last_name = [u'军', u'勇', u'伟', u'超', u'俊', u'君', u'敏', u'婷', u'纯', u'霜']
def createName():
	index1 = random.randint(0, 7)
	index2 = random.randint(0, 9)
	index3 = random.randint(0, 9)
	return first_name[index1] + last_name[index2] + last_name[index3]
	
# 随机生成性别
def createGender():
	return random.randint(0, 1)
	
# 随机生成地址
cities = [u'江苏省南京市', u'江苏省镇江市', u'江苏省无锡市', u'江苏省常州市']
def createAddress():
	return cities[random.randint(0, 3)]
	
# 随机生成职称
ranks = [u'教授', u'副教授', u'讲师']
def createRank():
	return ranks[random.randint(0, 2)]

# 生成学号
student_id = np.arange(141110001, 141110101, 1)

# 随机生成学生信息
student_infos = []
for i in range(0, 100):
	student_infos.append(( \
		student_id[i], createName(), \
		createGender(), u'电子科学与工程学院', \
		u'电子信息科学与技术', 14, \
		u'汉族', createAddress(), createPhoneNum()))

# 生成账号信息
student_accounts = []
for i in range(0, 100):
	student_accounts.append((student_id[i], 'test', student_id[i]))

# 生成工号
teacher_ids = np.arange(1, 11, 1)
	
# 随机生成教师信息
teacher_infos = []
for i in range(0, 10):
	teacher_infos.append((teacher_ids[i], createName(), \
		createGender(), u'电子科学与工程学院', \
		createRank(), createPhoneNum()))

conn = Connection.getConnection()
cursor = conn.cursor()
cursor.execute("select * from teach")
resultList = cursor.fetchall()

# 生成课程信息
course_infos = [\
	(1, u'计算方法', u'仙林校区 逸B-105', u'周二 第5-7节 1-18周', u'选修', u'电子科学与工程学院'), \
	(2, u'微波测量实验', u'仙林校区 仙林电子楼239室', u'周五 第5-6节 1-18周', u'核心', u'电子科学与工程学院'), \
	(3, u'操作系统', u'仙林校区 仙Ⅰ-115', u'周一 第3-4节 1-18周', u'选修', u'电子科学与工程学院'), \
	(4, u'矩阵计算与应用', u'仙林校区 仙Ⅰ-115', u'周一 第9-10节 1-18周', u'选修', u'电子科学与工程学院'), \
	(5, u'IT企业创业与发展战略', u'仙林校区 仙Ⅱ-304', u'	周二 第9-10节 1-18周', u'选修', u'电子科学与工程学院'), \
	(6, u'数据通信', u'仙林校区 仙Ⅰ-206', u'	周四 第5-7节 1-18周', u'选修', u'电子科学与工程学院'), \
	(7, u'微电子工艺', u'仙林校区 仙Ⅰ-104', u'周一 仙Ⅰ-104 1-18周', u'选修', u'电子科学与工程学院'), \
	(8, u'数字集成电路设计', u'仙林校区 仙Ⅰ-115', u'周一 第5-7节 1-12周', u'选修', u'电子科学与工程学院'), \
	(9, u'电子系统实践', u'仙林校区 仙Ⅰ-115 ', u'周一 第5-7节 1-12周', u'选修', u'电子科学与工程学院'), \
	(10, u'碳基电子学', u'仙林校区 仙Ⅱ-116', u'周三 第5-6节 1-18周', u'选修', u'电子科学与工程学院') \
]

# 随机生成选课信息
selection = []
for id in student_id:
	select = random.sample([i + 1 for i in range(10)], 5)
	for i in select:
		selection.append((id, i))

# 随机生成授课信息
teach = []
for id in teacher_ids:
	t = random.sample([i + 1 for i in range(10)], 3)
	for i in t:
		teach.append((id, i))

if (len(resultList) == 0):
	# 插入学生表信息
	cursor.executemany("insert into student values( \
		?, ?, ?, ?, ?, ?, ?, ?, ?)", student_infos)
		
	# 插入账号信息
	cursor.executemany("insert into student_account values( \
		?, ?, ?)", student_accounts)
		
	# 插入教师信息
	cursor.executemany("insert into teacher values( \
		?, ?, ?, ?, ?, ?)", teacher_infos)
		
	# 插入课程信息
	cursor.executemany("insert into course values( \
		?, ?, ?, ?, ?, ?)", course_infos)
	
	# 插入选课信息
	cursor.executemany("insert into selection values( \
		?, ?)", selection)
		
	# 插入授课信息
	cursor.executemany("insert into teach values( \
		?, ?)", teach)
	
	conn.commit()
	print 'done'

conn.close()