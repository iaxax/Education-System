create table course(
	course_id	integer primary key,
	name		varchar(10) NOT NULL,
	classroom	varchar(50) NOT NULL,
	classtime	varchar(50) NOT NULL,
	type		char(10) NOT NULL,
	department	char(10) NOT NULL
);

create table student(
	student_id	integer primary key,
	name		varchar(10) NOT NULL,
	gender		integer NOT NULL,
	department	varchar(10) NOT NULL,
	profession	varchar(10) NOT NULL,
	grade		integer NOT NULL,
	nation		char(10) NOT NULL,
	birthplace	varchar(50) NOT NULL,
	phone		char(11)
);

create table teacher(
	employee_id	integer primary key,
	name		varchar(10) NOT NULL,
	gender		integer NOT NULL,
	department	char(10) NOT NULL,
	rank		char(10) NOT NULL,
	phone		char(11)
);

create table selection(
	student_id	integer NOT NULL,
	course_id	integer NOT NULL,
	foreign key(student_id) references student(student_id),
	foreign key(course_id) references course(course_id)
);

create table teach(
	teacher_id integer NOT NULL,
	course_id integer NOT NULL,
	foreign key(teacher_id) references teacher(teacher_id),
	foreign key(course_id) references course(course_id)
);

create table student_account(
	username varchar(10) NOT NULL,
	password varchar(50) NOT NULL,
	student_id	integer NOT NULL,
	foreign key(student_id) references student(student_id)
);
