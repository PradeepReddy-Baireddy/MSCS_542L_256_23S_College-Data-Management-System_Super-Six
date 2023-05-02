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

CREATE TABLE Student_Info (
Student_ID INT PRIMARY KEY,
Address VARCHAR(45),
Father_Name VARCHAR(45),
Mother_Name VARCHAR(45),
FOREIGN KEY (Student_ID)
REFERENCES student(Student_ID)
);

CREATE TABLE Mail_ID(
Student_ID INT NOT NULL,
Mail_ID VARCHAR(45) PRIMARY KEY,
FOREIGN KEY (Student_ID)
REFERENCES Student_Info(Student_ID)
);

CREATE TABLE Phone_Numbers(
Student_ID INT NOT NULL,
mobile1 CHAR(10) PRIMARY KEY,
FOREIGN KEY (Student_ID)
REFERENCES student_info(Student_ID)
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


set foreign_key_checks=0;

INSERT INTO Admissions (Student_ID, Admission_Number, Application_Date, Decision_Date, Test_Written, Test_Score, Enrollment_Status)
VALUES (20220301, 'MR001', '2022-01-01', '2022-01-15', 'IELTS', 7.5, 'Enrolled'),
(20220302, 'MR002', '2022-02-01', '2022-06-15', 'IELTS', 7, 'Enrolled'),
(20220304, 'MR003', '2022-01-03', '2022-06-15', 'IELTS', 6.5, 'Enrolled'),
(20220305, 'MR004', '2022-07-01', '2022-06-15', 'GRE', 295, 'Enrolled'),
(20220306, 'MR005', '2022-05-09', '2022-06-15', 'IELTS', 7, 'Enrolled'),
(20220303, 'MR006', '2022-04-01', '2022-06-16', 'TOEFL', 110, 'Enrolled'),
(20220307, 'MR007', '2022-02-03', '2022-06-16', 'PTE', 75, 'Enrolled'),
(20220311, 'MR008', '2022-05-06', '2022-06-16', 'GRE', 312, 'Enrolled'),
(20220312, 'MR009', '2022-05-05', '2022-06-16', 'IELTS', 6.5, 'Enrolled'),
(20220315, 'MR010', '2022-06-09', '2022-06-16', 'PTE', 78, 'Enrolled');

INSERT INTO Hostel (Hostel_ID, Hostel_Name, Room_Number, Amenities, Vacancy, Price_Range)
VALUES ('LE-005', 'LEO HALL', '005', 'WiFi', 'Available', 2000),
('LE-006', 'LEO HALL', '006', 'WiFi', 'Available', 2000),
('LE-009', 'LEO HALL', '009', 'WiFi', 'Available', 2000),
('LE-010', 'LEO HALL', '010', 'WiFi', 'Available', 2000),
('MI-007', 'MIDRISE HALL', '007', 'WiFi, AC, Gym', 'Available', 4000),
('MI-008', 'MIDRISE HALL', '008', 'WiFi, AC, Gym', 'Available', 4000),
('MI-009', 'MIDRISE HALL', '009', 'WiFi, AC, Gym', 'Available', 4000),
('MA-005', 'MARIUM HALL', '005', 'WiFi, AC', 'Available', 3000),
('MA-006', 'MARIUM HALL', '006', 'WiFi, AC', 'Available', 3000),
('MA-001', 'MARIUM HALL', '001', 'WiFi, AC', 'Available', 3000),
('MA-009', 'MARIUM HALL', '009', 'WiFi, AC', 'Available', 3000),
('CH-004', 'CHAMPAGNAT HALL', '004', 'WiFi, AC, Gym', 'Available', 3500),
('CH-005', 'CHAMPAGNAT HALL', '005', 'WiFi, AC, Gym', 'Available', 3500),
('SH-007', 'SHEAHAN HALL', '007', 'WiFi, Gym', 'Available', 2500),
('SH-003', 'SHEAHAN HALL', '003', 'WiFi, Gym', 'Available', 2500);




INSERT INTO Departments (Dept_ID, Dept_name, Courses_offered, HOD, Office_Location)
VALUES ('DT_CS', 'Computer Science', 'DBMS,Programming, Algorithms, Data Structures', 'Jennifer Lawrence', 'Marist, Donnelly, Room 101'),
('DT_MH', 'MECHANICAL', 'Programming, Algorithms, Data Structures', 'JOHN WICK', 'MARIST, Hancock, Room 101'),
('DT_BT', 'BIO-TECH', 'Programming, Algorithms, Data Structures', 'JOHN WICK', 'MARIST, Hancock, Room 101'),
('DT_EL', 'ELECTRICAL', 'Programming, Algorithms, Data Structures', 'JOHN WICK', 'MARIST, Hancock, Room 101'),
('DT_AR', 'ARTS', 'Programming, Algorithms, Data Structures', 'JOHN WICK', 'MARIST, Hancock, Room 101');




INSERT INTO Programs (Program_ID, Program_Name, credits_required, Duration, Number_of_courses, Dept_ID, Tuition_Fee)
VALUES ('BS_CS', 'Bachelor of Science in Computer Science', 120, '4 years', 40, 'DT_CS', 80000),
('BS_DG', 'Bachelor of Design', 100, '4 years', 34, 'DT_DG', 90000),
('BS_BF', 'Bachelor of  Banking and Finance', 120, '4 years', 36, 'DT_BF', 80000),
('BS_ATS', 'Bachelor of Arts', 120, '4 years', 33, 'DT_ATS', 88000),
('BS_BK', 'Bachelor of Banking', 90, '3 years', 34, 'DT_BK', 78000),
('BS_IS', 'Bachelor of Science in Informantion systems', 80, '3 years', 36, 'DT_IS', 72000),
('BS_AC', 'Bachelor of Accounting', 130, '4 years', 30, 'DT_AC', 100000),
('BS_MC', 'Bachelor of Music ', 140, '4 years', 44, 'DT_MC', 120000),
('BS_BMS', 'Bachelor of Biomedical science', 110, '4 years', 42, 'DT_BMS', 70000),
('BS_FA', 'Bachelor of Fine Arts ', 126, '4 years', 40, 'DT_FA', 84000);



INSERT INTO Student (Student_ID, Student_Name, Gender, Program_type, DOB, Age, Hostel_ID, CGPA, Admission_Number)
VALUES (20220301, 'Olivia Wilde', 'F', 'BS_CS', '1978-03-01', 45, 'LE-005', 3.5, 'MR001'),
(20220302, 'Reese Witherspoon', 'F', 'BS_DG', '1959-05-03', 64, 'LE-006', 3.7, 'MR003'),
(20220304, 'Bruno Mars', 'M', 'BS_BMS', '1980-12-05', 42, 'MI-009', 3.6, 'MR009'),
(20220305, 'Gigi Hadid', 'F', 'BS_CS', '1983-11-07', 39, 'CH-004', 3.5, 'MR006'),
(20220306, 'Katy Perry', 'F', 'BS_MC', '1979-04-06', 44, 'LE-010', 3.2, 'MR004'),
(20220303, 'Natalie Portman', 'F', 'BS_CS', '1985-01-23', 37, 'SH-007', 3.1, 'MR002'),
(20220312, 'Demi Moore', 'F', 'BS_FA', '1979-03-02', 41, 'MA-006', 3.0, 'MR008'),
(20220307, 'Joaquin Pheonix', 'F', 'BS_CS', '1969-04-06', 54, 'MI-008', 3.9, 'MR007'),
(20220311, 'Kit Harington', 'M', 'BS_MC', '1973-06-15', 29, 'MA-009', 3.3, 'MR010'),
(20220315, 'Harry Potter', 'M', 'BS_IS', '1989-11-11', 34, 'SH-003', 3.7, 'MR005');


INSERT INTO Phone_Numbers (Student_ID, mobile1)
VALUES (20220302, '8457639475'),
(20220307, '8457737537'),
(20220304, '8478958653'),
(20220311, '8540832865'),
(20220306, '8974605198'),
(20220305, '8867489509'),
(20220315, '9778477494'),
(20220303, '8475874994'),
(20220301, '9764838759'),
(20220312, '8476767485');




INSERT INTO Mail_ID (Student_ID, Mail_ID)
VALUES (20220301, '0livia.wilde@gmail.com'),
(20220311, 'kit.haringtone@gmail.com'),
(20220307, 'Joaquin.Pheonix@gmail.com'),
(20220315, 'Harry.Potter@marist.edu'),
(20220312, 'Demi.Moore@marist.edu'),
(20220306, 'Katy.Perry1979@marist.edu'),
(20220303, 'Nat.man@gmail.com'),
(20220305, 'Gigi.Hadid@marist.edu'),
(20220302, 'Reese.Witherspoon@marist.edu'),
(20220304, 'Bruno.Mars@marist.edu');




INSERT INTO Student_Info (Student_ID, Address, Father_Name, Mother_Name)
VALUES (20220301, '123 Main St., Anytown, USA', 'Bob Smith', 'Jane Smith'),
(20220311,'45 Noth clover USA','jack harington','jane harington'),
(20220307,'29 orchid ,USA, 12605','Dark Pheonix','Light Pheonix'),
(20220304,null,null,null),
(20220305,null,'True Hadid','false Hadid'),
(20220302,'75 Vernon street, NY ,USA',null,null),
(20220315,'Hogwarts, England','James Potter','Lily Potter'),
(20220306,null,'john perry','Don perry'),
(20220312,'24 Main street,USA','Yes Moore','No moore'),
(20220303,null,null,null);




INSERT INTO Courses (Course_ID, Course_Name, Duration, Credits, Course_desc)
VALUES ('542L', 'DBMS', 6, 4, 'This course covers the basics of DataBaseManagement'),
('560L', 'Networking', 6, 4, 'Netwotk designing'),
('501L', 'OOP', 4, 8, 'Ojective oriented programming'),
('521s', 'Data Mining', 10, 4, 'data extraction'),
('522s', 'Emerging Technologies', 6, 6, 'About Trending technologies'),
('570F', 'Accounting', 12, 4, 'Manage Accounts'),
('580F', 'Commication systems', 6, 4, null),
('520G', 'Designing object', 6, 4, 'plan for designing'),
('578A', 'Law Fundamentals', 18, 8, 'Fundamentals of law'),
('530C', 'Acoustics', 4, 4, 'Sound sytems'),
('540B', 'Anatomy', 12, 12, 'Human beings');


INSERT INTO Program_has_Courses (Course_ID, Program_ID)
VALUES ('542L', 'BS_CS'),
('542L', 'BS_IS'),
('560L','BS_CS'),
('560L','BS_IS'),
('501L','BS_CS'),
('521s', 'BS_IS'),
('522s', 'BS_IS'),
('522s', 'BS_MC'),
('570F', 'BS_BF'),
('570F', 'BS_IS'),
('580F', 'BS_BF'),
('520G', 'BS_DG'),
('578A', 'BS_ATS'),
('530C', 'BS_MC'),
('540B', 'BS_BMS');

INSERT INTO Faculty (Fac_ID, Faculty_Name, Designation, Office_hours, Dept_ID)
VALUES ('FAC001', 'Reza Sadeghi', 'Professor', 'Monday 9-11am, Wednesday 1-3pm', 'DT_CS'),
('FAC002', 'Micheal Gildimi', 'Professor', 'Monday 9-11am, Wednesday 1-3pm', 'DT_MH'),
('FAC003', 'Sandhya Aneja', 'Juniopr Lecteror', 'Monday 2-5pm', 'DT_BT'),
('FAC004', 'Jennifer Lawrence', 'HOD', 'Monday 2-5pm', 'DT_EL'),
('FAC005', 'Vishwanath Anand', 'proffesor', 'Monday 2-5pm', 'DT_AR');


INSERT INTO Sessions (Session_ID, Class_Location, Faculty_ID, Course_ID, Timings, Duration)
VALUES (5001, 'Donnelly, Room 201', 'FAC002', '501L', 'Jan 9th ,2022,6:00 pm', 2),
(5002, 'Donnelly, Room 201', 'FAC002', '501L', 'Jan 16th ,2022, 6:00 pm', 2),
(5003, 'Donnelly, Room 201', 'FAC002', '501L', 'Jan 23th ,2022, 6:00 pm', 2),
(6001, 'Hancock, Room 501', 'FAC001', '542L', 'Jan 20th ,2023, 6:30 pm', 3),
(6002, 'Hancock, Room 501', 'FAC001', '542L', 'Jan 27th ,2023, 6:30 pm', 3),
(6003, 'Hancock, Room 501', 'FAC001', '542L', 'Feb 4th ,2023, 6:30 pm', 3),
(6004, 'Hancock, Room 501', 'FAC001', '542L', 'Feb 11th ,2023 ,6:30 pm', 3),
(7001, 'Lowell thomas, Room 601', 'FAC003', '560L', 'Jan 19th ,2023, 3:30 pm', 3),
(7002, 'Lowell thomas, Room 601', 'FAC003', '560L', 'Jan 26th ,2023, 3:30 pm', 3);

INSERT INTO Class_room (Class_ID, Session_ID)
VALUES ('DON-201', 5001),
('DON-201', 5002),
('DON-201', 5003),
('HAN-201', 6001),
('HAN-201', 6002),
('HAN-201', 6003),
('HAN-201', 6004),
('LOW-601', 7001),
('LOW-601', 7002);

INSERT INTO Grades_and_Attendance (Student_ID, Session_ID, Assignment_Score, Lab_score, Attendance, Quiz_Score, Student_grades, Class_ID)
VALUES (20220301, 5001, 80, 90, 'P', 75, 'B+', 'DON-201'),
(20220301, 5002, 60, 70, 'P', 75, 'C+', 'DON-201'),
(20220301, 5003, 50, 60, 'P', 75, 'D+', 'DON-201'),
(20220302, 5001, 90, 95, 'P', 75, 'A+', 'DON-201'),
(20220302, 5002, 80, 90, 'P', 75, 'B+', 'DON-201'),
(20220302, 5003, 50, 65, 'P', 75, 'D', 'DON-201'),
(20220305, 5001, 90, 90, 'P', 75, 'A', 'DON-201'),
(20220305, 5002, 80, 90, 'P', 75, 'B+', 'DON-201'),
(20220305, 5003, 60, 75, 'P', 75, 'C', 'DON-201');

set foreign_key_checks=1;

