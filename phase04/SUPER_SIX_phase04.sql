CREATE DATABASE IF NOT EXISTS SUPER_SIX;
USE SUPER_SIX;

CREATE TABLE Admissions (
Student_ID INT NOT NULL,
Admission_Number VARCHAR(45) PRIMARY KEY,
Application_Date DATETIME,
Decision_Date DATETIME,
Test_Written VARCHAR(45),
Test_Score INT,
Enrollment_Status VARCHAR(45)
);

CREATE TABLE Hostel (
Hostel_ID VARCHAR(45) PRIMARY KEY,
Hostel_Name VARCHAR(45) NOT NULL,
Room_Number VARCHAR(45),
Amenities VARCHAR(45),
Vacancy VARCHAR(45),
Price_Range INT
);

CREATE TABLE Departments (
Dept_ID VARCHAR(45) PRIMARY KEY,
Dept_name VARCHAR(45) NOT NULL,
Courses_offered VARCHAR(45) NOT NULL,
HOD VARCHAR(45),
Office_Location VARCHAR(45)
);

CREATE TABLE Programs (
Program_ID VARCHAR(45) PRIMARY KEY,
Program_Name VARCHAR(45) NOT NULL,
credits_required INT NOT NULL,
Duration VARCHAR(45),
Number_of_courses INT,
Dept_ID VARCHAR(45) NOT NULL,
Tuition_Fee INT,
FOREIGN KEY (Dept_ID)
REFERENCES Departments (Dept_ID)
);

CREATE TABLE Student (
Student_ID INT PRIMARY KEY,
Student_Name VARCHAR(45) NOT NULL,
Gender CHAR(1),
Program_type VARCHAR(45) NOT NULL,
DOB DATETIME NOT NULL,
Age INT,
Hostel_ID VARCHAR(45),
CGPA DECIMAL(4,2),
Admission_Number VARCHAR(45) NOT NULL,
FOREIGN KEY (Admission_Number)
REFERENCES Admissions (Admission_Number),
FOREIGN KEY (Hostel_ID)
REFERENCES Hostel (Hostel_ID),
FOREIGN KEY (Program_type)
REFERENCES Programs (Program_ID)
);

CREATE TABLE Phone_Numbers(
Student_ID INT PRIMARY KEY,
mobile1 long NOT NULL,
mobile2 long,
mobile3 long,
mobile4 long,
FOREIGN KEY (Student_ID)
REFERENCES student(Student_ID)
);

CREATE TABLE Mail_ID(
Student_ID INT PRIMARY KEY,
Mail_ID1 VARCHAR(45) NOT NULL,
Mail_ID2 VARCHAR(45),
Mail_ID3 VARCHAR(45),
Mail_ID4 VARCHAR(45),
FOREIGN KEY (Student_ID)
REFERENCES student(Student_ID)
);

CREATE TABLE Student_Info (
Student_ID INT PRIMARY KEY,
Mail VARCHAR(45),
Phone VARCHAR(45),
Address VARCHAR(45),
Father_Name VARCHAR(45),
Mother_Name VARCHAR(45),
FOREIGN KEY (Student_ID)
REFERENCES student(Student_ID),
FOREIGN KEY (Student_ID)
REFERENCES Phone_Numbers(Student_ID),
FOREIGN KEY (Student_ID)
REFERENCES Mail_ID(Student_ID)
);


CREATE TABLE Courses (
Course_ID VARCHAR(45) PRIMARY KEY,
Course_Name VARCHAR(45) NOT NULL,
Duration INT,
Credits INT NOT NULL,
Course_desc VARCHAR(100)
);


CREATE TABLE Program_has_Courses(
Course_ID VARCHAR(45),
Program_ID VARCHAR(45),
PRIMARY KEY(Course_ID,Program_ID),
FOREIGN KEY (Course_ID)
REFERENCES Courses(Course_ID),
FOREIGN KEY (Program_ID)
REFERENCES Programs(Program_ID)
);


CREATE TABLE Faculty (
Fac_ID VARCHAR(45) PRIMARY KEY,
Faculty_Name VARCHAR(45) NOT NULL,
Designation VARCHAR(45),
Office_hours VARCHAR(45),
Dept_ID VARCHAR(45) NOT NULL,
FOREIGN KEY (Dept_ID)
REFERENCES Departments (Dept_ID)
);

CREATE TABLE Faculty_teaches_Classes(
Fac_ID VARCHAR(45),
Course_ID VARCHAR(45),
PRIMARY KEY (Fac_ID, Course_ID),
FOREIGN KEY (Course_ID)
REFERENCES Courses(Course_ID),
FOREIGN KEY (Fac_ID)
REFERENCES Faculty(Fac_ID)
);


CREATE TABLE Sessions (
Session_ID INT PRIMARY KEY,
Class_Location VARCHAR(100),
Faculty_ID VARCHAR(45) NOT NULL,
Course_ID VARCHAR(45) NOT NULL,
Timings varchar(45),
Duration INT,
FOREIGN KEY (Faculty_ID, Course_ID)
REFERENCES Faculty_teaches_Classes (Fac_ID, Course_ID)
);

CREATE TABLE Class_room(
Class_ID VARCHAR(45) NOT NULL,
Session_ID INT NOT NULL,
PRIMARY KEY (Class_ID,Session_ID),
FOREIGN KEY (Session_ID)
REFERENCES Sessions(Session_ID)
);

CREATE TABLE Grades_and_Attendance (
Student_ID INT NOT NULL,
Session_ID INT NOT NULL,
Assignment_Score INT,
Lab_score INT,
Attendance VARCHAR(45),
Quiz_Score INT,
Student_grades CHAR(2) NOT NULL,
Class_ID VARCHAR(45),
PRIMARY KEY (Student_ID, Session_ID),
FOREIGN KEY (Student_ID)
REFERENCES Student(Student_ID),
FOREIGN KEY (Session_ID)
REFERENCES Sessions (Session_ID),
FOREIGN KEY (Class_ID)
REFERENCES Class_room(Class_ID)
);

CREATE TABLE Student_has_grades(
Student_ID INT NOT NULL,
Student_grades CHAR(2) NOT NULL,
PRIMARY KEY(Student_ID,Student_grades),
FOREIGN KEY (Student_ID)
REFERENCES Student(Student_ID)
);

