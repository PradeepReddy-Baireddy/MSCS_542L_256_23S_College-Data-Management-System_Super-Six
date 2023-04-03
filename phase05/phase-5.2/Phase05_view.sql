
create view student_grades
as select S.Session_ID,Course_ID,timings,Assignment_score,Lab_score,Quiz_Score,Student_grades
from Grades_and_attendance G
join
Sessions S on G.Session_ID=S.Session_ID
where Student_ID=20220301;

-------
create view admission_info
as select S.Student_ID,S.Student_name,A.Admission_Number,A.enrollment_status from Admissions A
join
Student S on S.Student_ID=A.student_ID
where S.Student_ID = 20220305;

-------
create view personal_info
as select Si.Father_Name,Si.Mother_Name,S.DOB,Si.Address from Student_Info Si
join
Student S on S.student_ID=Si.Student_ID
where S.Student_ID=20220302;

-------
create view Contact_Info
as select p.mobile1,p.mobile2,p.mobile3,p.mobile4,m.mail_id1,m.mail_id2,m.mail_id3,m.mail_id4
from Phone_Numbers p
join
Mail_ID m on m.student_ID=p.student_ID
where m.student_ID=20220311;

-------
create view programs_offered_by_department
as select D.Dept_Name,P.Program_name,P.credits_required from Programs P
join 
Departments D on D.Dept_ID=P.Dept_ID
where P.Dept_ID='DT_CS';

--------

create view courses_in_program
as select C.Course_ID,C.Course_Name,C.Course_desc as about_course
from Courses C
left join
Program_has_Courses p on p.Course_ID=C.course_ID
where p.program_ID='BS_IS';

--------
create view class_info
as select S.Student_ID,S.Student_Name from Student S
join
Grades_and_Attendance G on S.Student_ID=G.Student_ID
where G.session_ID=5001;
