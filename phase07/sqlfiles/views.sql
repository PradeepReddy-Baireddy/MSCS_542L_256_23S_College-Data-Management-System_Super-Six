use super_six;


create view student_grades
as select S.Session_ID,Course_ID,timings,Assignment_score,Lab_score,Quiz_Score,Student_grades
from Grades_and_attendance G
join
Sessions S on G.Session_ID=S.Session_ID;

select * from student_grades;

-------
create view admission_info
as select S.Student_ID,S.Student_name,A.Admission_Number,A.enrollment_status from Admissions A
join
Student S on S.Student_ID=A.student_ID;

select * from admission_info;

-------
create view personal_info
as select Si.Father_Name,Si.Mother_Name,S.DOB,Si.Address from Student_Info Si
join
Student S on S.student_ID=Si.Student_ID;

select * from personal_info;

-------
create view Contact_Info
as select p.mobile1,m.mail_id
from Phone_Numbers p
join
Mail_ID m on m.student_ID=p.student_ID;

select * from contact_info;

-------
create view programs_offered_by_department
as select D.Dept_Name,P.Program_name,P.credits_required from Programs P
join 
Departments D on D.Dept_ID=P.Dept_ID;

select * from programs_offered_by_Department;

--------

create view courses_in_program
as select C.Course_ID,C.Course_Name,C.Course_desc as about_course
from Courses C
left join
Program_has_Courses p on p.Course_ID=C.course_ID;

select * from courses_in_program;

--------
create view class_info
as select S.Student_ID,S.Student_Name from Student S
join
Grades_and_Attendance G on S.Student_ID=G.Student_ID;

select * from class_info;