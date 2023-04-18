import tkinter as tk
from tkinter import Scrollbar, messagebox
import mysql.connector


def OpenMain(window,db):
    global win
    global database
    global admin
    database = db
    win = window
    if(db.user == "root"):
        admin = True
    else:
        admin = False
    MainPage()

def show_hostel():
    sampletDeletionPage("Hostel","Hostel","Hostel")

def clearwindow():
    list = win.pack_slaves()
    for i in list:
        i.destroy()

def exit(*window1):
    if(len(window1) != 0):
        win.destroy()
        return
    clearwindow()
    MainPage()


def LoginPage():
    clearwindow()
    cur = database.cursor()
    win.title("Login Page")
    def login():
        username = True
        cur.execute('SELECT * FROM student')
        for i in cur.fetchall():
            if str(i[0]) == username_entry.get():
                if str(i[1]) != password_entry.get():
                    messagebox.showerror(title="Error", message="Invalid Password")
                    return
                else:
                    list = win.pack_slaves()
                    for j in list:
                        j.destroy()
                    StudentLoginPage(str(i[0]))
                    messagebox.showinfo(title="Successfully loggedIn", message="You have successfully logged in.")
                username = False
                break
            else:
                username = True
        if username == True:
            messagebox.showerror(title="Error", message="Invalid Username")
            return
    frame = tk.Frame()

    tk.Label(frame, text="Login").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)

    tk.Label(frame, text="Username").grid(row=1, column=0)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1, pady=20)

    tk.Label(frame, text="Password").grid(row=2, column=0)
    password_entry = tk.Entry(frame)
    password_entry.grid(row=2, column=1, pady=20)

    tk.Button(frame, text="Login", command=login).grid(row=3, column=0, columnspan=2, pady=30)
    tk.Button(frame,text="Exit",command=exit).grid(row = 4,column=0,columnspan=3)

    frame.pack()





def AdmissionsPage():
    clearwindow()
    cur = database.cursor()
    win.title("Get Admission Status")
    def admissions():
        admission = False
        cur.execute('SELECT * FROM admissions')
        for i in cur.fetchall():
            if str(i[1]) == str(AdmissionID_entry.get()):
                if str(i[6]) == "Enrolled":
                    messagebox.showinfo(title="Status", message="Enrolled")
                else:
                    messagebox.showinfo(title="Status", message="Awaiting")
                admission = True
                break
        if admission == False:
            messagebox.showerror(title="Error", message="Enter Valid Admission Number")
    frame = tk.Frame()
    tk.Label(frame, text="Admission").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)
    tk.Label(frame, text="Admission ID").grid(row=1, column=0)
    AdmissionID_entry = tk.Entry(frame)
    AdmissionID_entry.grid(row=1, column=1, pady=20)
    tk.Button(frame, text="Get status", command=admissions).grid(row=2, column=0, columnspan=2, pady=30)
    tk.Button(frame,text="Exit",command=exit).grid(row = 3,column=0,columnspan=3)
    frame.pack()




def StudentLoginPage(id):
    cur = database.cursor()
    win.title("Student Login")
    frame = tk.Frame()
    def ProfileDetails():
        cur.execute("select * from student_info where student_ID = "+id)
        data = cur.fetchall()
        data = list(data[0])
        index = 0
        for i in data:
            if(i == None):
                data[index]="None"
            index+=1
        tk.Label(frame, text="Father Name :" +data[4]).grid(row=2, column=1, pady=20,sticky="w")
        tk.Label(frame, text="Mother Name :"+data[5]).grid(row=3, column=1,sticky="w")
    def SessionsDetails():
        print("progressing")
    tk.Label(frame, text="Student_Login").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)
    tk.Button(frame, text="Profile",command = ProfileDetails).grid(row=1, column=0, padx=10)
    tk.Button(frame, text="Courses",command =lambda: CoursesPage(id)).grid(row=1, column=1, padx=10)
    tk.Button(frame, text="Sessions",command = SessionsDetails).grid(row=1, column=2, padx=10)
    tk.Button(frame, text="Logout",command = exit).grid(row=1, column=3, padx=10)
    frame.pack()


def MainPage():  
    
    welcome_label = tk.Label(win, text="Welcome to Marist College!", font=("Arial", 20))
    welcome_label.pack(pady=20)

    admissions_button = tk.Button(win, text="Admissions", command=AdmissionsPage, width=20)
    admissions_button.pack(pady=10)

    programs_button = tk.Button(win, text="Programs", command=lambda:sampletDeletionPage("Programs","Programs","main"), width=20)
    programs_button.pack(pady=10)

    departments_button = tk.Button(win, text="Departments", command=lambda:sampletDeletionPage("Department","Departments","main"), width=20)
    departments_button.pack(pady=10)

    login_button = tk.Button(win, text="Student Login", command=LoginPage, width=20)
    login_button.pack(pady=10)

    hostel_button = tk.Button(win, text="Hostel", command=show_hostel, width=20)
    hostel_button.pack(pady=10)

    Change_Password_button = tk.Button(win, text="Change Password", command=ChangeUserPassword, width=20)
    Change_Password_button.pack(pady=10)   

    if(admin == True):
        User_button = tk.Button(win, text="Create New User", command=createuser, width=20)
        User_button.pack(pady=10)  
        Remove_button = tk.Button(win, text="Remove User", command=RemoveUser, width=20)
        Remove_button.pack(pady=10)        
        Insert_button = tk.Button(win, text="Insertion", command=InsertionPage, width=20)
        Insert_button.pack(pady=10)
        view_button = tk.Button(win, text="View/search and Deletion", command=DeletionPage, width=20)
        view_button.pack(pady=10)
        Alter_table = tk.Button(win, text="Alter Table", command=AlterTable, width=20)
        Alter_table.pack(pady=10) 
        Change_normal_Password_button = tk.Button(win, text="Change Normal Password", command=ChangeNormalUserPassword, width=20)
        Change_normal_Password_button.pack(pady=10) 
    
    Exit_button = tk.Button(win, text="Exit", command=lambda: exit("window"), width=20)
    Exit_button.pack(pady=10)


def ChangeNormalUserPassword():
    clearwindow()
    cur = database.cursor()
    win.title("Change Password")
    frame = tk.Frame()
    def change():
        tempstring1 = "Alter user '"+username_entry.get()+"'@'localhost' identified by '"+password_entry.get()+"';"
        try:
            cur.execute(tempstring1)
            database.commit()
        except Exception as e:
            print(e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="Password changed successfully")
            exit()

    frame = tk.Frame()
    tk.Label(frame, text="Change Password").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)

    tk.Label(frame, text="Username").grid(row=1, column=0)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1, pady=20)

    tk.Label(frame, text="New Password").grid(row=2, column=0)
    password_entry = tk.Entry(frame)
    password_entry.grid(row=2, column=1, pady=20)

    tk.Button(frame, text="Change", command=change).grid(row=3, column=0, columnspan=2, pady=30)

    Exit_button = tk.Button(win, text="Exit", command=exit, width=20)
    Exit_button.pack(pady=10)

    frame.pack()


def ProgramsPage():
    clearwindow()
    cur = database.cursor()
    win.title("Programs Offered")
    frame = tk.Frame()
    cur.execute("select * from programs")
    programlist = cur.fetchall()
    tk.Label(frame, text="Programs_Offered").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)
    tk.Label(frame, text="Programs IDs").grid(row=1,column=0,sticky="w")
    tk.Label(frame, text="--------------").grid(row=2,column=0,sticky="w")
    tk.Label(frame, text="Programs Name").grid(row=1,column=1,sticky="w")
    tk.Label(frame, text="---------------------").grid(row=2,column=1,sticky="w")
    r=3
    for i in programlist:
        tk.Label(frame, text = i[0]).grid(row=r, column=0, sticky="w")
        tk.Label(frame, text = i[1]).grid(row=r, column=1, sticky="w")
        r=r+1
    tk.Button(frame,text= "Return",command= exit,width=20).grid(row=r,column=1,pady=30)
    frame.pack()




def CoursesPage(*id):
    clearwindow()
    cur = database.cursor()
    frame = tk.Frame()
    if len(id) == 0:
        cur.execute("select * from courses")
    else:
        cur.execute("select * from courses c join program_has_courses pc on pc.Course_ID = c.Course_ID join student s on s.program_type = pc.Program_ID where student_ID ="+id[0])
    courseList = cur.fetchall()
    tk.Label(frame, text="Courses").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)
    tk.Label(frame, text="Courses IDs").grid(row=1,column=0,sticky="w")
    tk.Label(frame, text="--------------").grid(row=2,column=0,sticky="w")
    tk.Label(frame, text="Courses Name").grid(row=1,column=1,sticky="w")
    tk.Label(frame, text="---------------------").grid(row=2,column=1,sticky="w")
    r=3
    for i in courseList:
        tk.Label(frame, text = i[0]).grid(row=r, column=0, sticky="w")
        tk.Label(frame, text = i[1]).grid(row=r, column=1, sticky="w")
        r=r+1
    tk.Button(frame,text= "Return",command= exit,width=20).grid(row=r,column=1,pady=30)
    frame.pack()

def createuser():
    clearwindow()
    cur = database.cursor()
    win.title("Create User")
    frame = tk.Frame()
    def create():
        tempstring1 = "create user if not exists '"+username_entry.get()+"'@'localhost' identified by '"+password_entry.get()+"';"
        tempstring2 = "GRANT create,alter,drop,select,update,insert on super_six.* to '"+username_entry.get()+"'@'localhost'"
        try:
            cur.execute(tempstring1)
            cur.execute(tempstring2)
            database.commit()
        except Exception as e:
            print(e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="New User Created.")
            exit()

    frame = tk.Frame()
    tk.Label(frame, text="Create user").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)

    tk.Label(frame, text="New Username").grid(row=1, column=0)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1, pady=20)

    tk.Label(frame, text="Password").grid(row=2, column=0)
    password_entry = tk.Entry(frame)
    password_entry.grid(row=2, column=1, pady=20)

    tk.Button(frame, text="Create", command=create).grid(row=3, column=0, columnspan=2, pady=30)
    tk.Button(frame, text="Exit", command=exit).grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()

def RemoveUser():
    clearwindow()
    cur = database.cursor()
    win.title("Create User")
    def Remove():
        try:
            if(username_entry != "root"):
                cur.execute("drop user if exists "+username_entry.get()+"@'localhost'")
                database.commit()
            else:
                exit()
                messagebox.showinfo(title="Error", message="Root user cannot be removed")
        except:
            print("Enter Valid data")
            exit()
        else:
            exit()
            messagebox.showinfo(title="Successful", message="User Removed")

    frame = tk.Frame()
    tk.Label(frame, text="Remove user").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)

    tk.Label(frame, text="Username").grid(row=1, column=0)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1, pady=20)

    tk.Button(frame, text="Remove", command=Remove).grid(row=3, column=0, columnspan=2, pady=30)

    Exit_button = tk.Button(win, text="Exit", command=exit, width=20)
    Exit_button.pack(pady=10)

    frame.pack()

def ChangeUserPassword():
    clearwindow()
    cur = database.cursor()
    win.title("Change Password")
    frame = tk.Frame()
    def change():
        tempstring1 = "Alter user CURRENT_USER() identified by '"+password_entry.get()+"';"
        try:
            cur.execute(tempstring1)
            database.commit()
        except Exception as e:
            print(e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="Password changed successfully")
            exit()

    frame = tk.Frame()
    tk.Label(frame, text="Change Password").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)

    tk.Label(frame, text="New Password").grid(row=2, column=0)
    password_entry = tk.Entry(frame)
    password_entry.grid(row=2, column=1, pady=20)

    tk.Button(frame, text="Change", command=change).grid(row=3, column=0, columnspan=2, pady=30)
    tk.Button(frame, text="Exit", command=exit).grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()








def InsertionPage():
    clearwindow()
    admissionquery = "INSERT INTO Admissions (Student_ID, Admission_Number, Application_Date, Decision_Date, Test_Written, Test_Score, Enrollment_Status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    studentquery = "INSERT INTO Student (Student_ID, Student_Name, Gender, Program_type, DOB, Age, Hostel_ID, CGPA, Admission_Number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    hostelquesry = "INSERT INTO Hostel (Hostel_ID, Hostel_Name, Room_Number, Amenities, Vacancy, Price_Range) VALUES (%s, %s, %s, %s, %s, %s)"
    departmentInsertion = "INSERT INTO Departments (Dept_ID, Dept_name, Courses_offered, HOD, Office_Location) VALUES (%s, %s, %s, %s, %s)"
    programquery = "INSERT INTO Programs (Program_ID, Program_Name, credits_required, Duration, Number_of_courses, Dept_ID, Tuition_Fee) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    coursequery = "INSERT INTO Courses (Course_ID, Course_Name, Duration, Credits, Course_desc) VALUES (%s, %s, %s, %s, %s)"
    sessionsquery = "INSERT INTO Sessions (Session_ID, Class_Location, Faculty_ID, Course_ID, Timings, Duration) VALUES (%s, %s, %s, %s, %s, %s)"
    faccultyquery = "INSERT INTO Faculty (Fac_ID, Faculty_Name, Designation, Office_hours, Dept_ID) VALUES (%s, %s, %s, %s, %s)"
    studentinfquery = "INSERT INTO Student_Info (Student_ID, Mail, Phone, Address, Father_Name, Mother_Name) VALUES (%s, %s, %s, %s, %s, %s)"
    student_button = tk.Button(win, text="Student", command=lambda: sampleInsertionPage(studentquery,"student"), width=20)
    student_button.pack(pady=10)
    Admission_button = tk.Button(win, text="Admissions", command=lambda: sampleInsertionPage(admissionquery,"Admissions"), width=20)
    Admission_button.pack(pady=10)
    Hostel_button = tk.Button(win, text="Hostel", command=lambda: sampleInsertionPage(hostelquesry,"hostel"), width=20)
    Hostel_button.pack(pady=10)
    Department_button = tk.Button(win, text="Department", command=lambda: sampleInsertionPage(departmentInsertion,"departments"), width=20)
    Department_button.pack(pady=10)
    Programs_button = tk.Button(win, text="Programs", command=lambda: sampleInsertionPage(programquery,"programs"), width=20)
    Programs_button.pack(pady=10)
    Sessions_button = tk.Button(win, text="Sessions", command=lambda: sampleInsertionPage(sessionsquery,"Sessions"), width=20)
    Sessions_button.pack(pady=10)
    Student_info_button = tk.Button(win, text="Student_info",command = lambda: sampleInsertionPage(studentinfquery,"student_info"), width=20)
    Student_info_button.pack(pady=10)
    Courses_button = tk.Button(win, text="Courses", command=lambda: sampleInsertionPage(coursequery,"Courses"), width=20)
    Courses_button.pack(pady=10)
    Faculty_button = tk.Button(win, text="Faculty", command=lambda: sampleInsertionPage(faccultyquery,"Faculty"), width=20)
    Faculty_button.pack(pady=10)
    Exit_button = tk.Button(win, text="Exit", command=exit, width=20)
    Exit_button.pack(pady=10)



def AlterTable():
    clearwindow()
    student_button = tk.Button(win, text="Student", command=lambda: AlterTablePage("student"), width=20)
    student_button.pack(pady=10)
    Admission_button = tk.Button(win, text="Admissions", command=lambda: AlterTablePage("Admissions"), width=20)
    Admission_button.pack(pady=10)
    Hostel_button = tk.Button(win, text="Hostel", command=lambda: AlterTablePage("hostel"), width=20)
    Hostel_button.pack(pady=10)
    Department_button = tk.Button(win, text="Department", command=lambda: AlterTablePage("departments"), width=20)
    Department_button.pack(pady=10)
    Programs_button = tk.Button(win, text="Programs", command=lambda: AlterTablePage("programs"), width=20)
    Programs_button.pack(pady=10)
    Sessions_button = tk.Button(win, text="Sessions", command=lambda: AlterTablePage("Sessions"), width=20)
    Sessions_button.pack(pady=10)
    Student_info_button = tk.Button(win, text="Student_info",command = lambda: AlterTablePage("student_info"), width=20)
    Student_info_button.pack(pady=10)
    Courses_button = tk.Button(win, text="Courses", command=lambda: AlterTablePage("Courses"), width=20)
    Courses_button.pack(pady=10)
    Faculty_button = tk.Button(win, text="Faculty", command=lambda: AlterTablePage("Faculty"), width=20)
    Faculty_button.pack(pady=10)
    Exit_button = tk.Button(win, text="Exit", command=exit, width=20)
    Exit_button.pack(pady=10)



def DeletionPage():
    clearwindow()
    Inserttstudent_button = tk.Button(win, text="Student", command=lambda:sampletDeletionPage("Deletion","student"), width=20)
    Inserttstudent_button.pack(pady=10)
    InserttAdmission_button = tk.Button(win, text="Admissions", command=lambda:sampletDeletionPage("Deletion","admissions"), width=20)
    InserttAdmission_button.pack(pady=10)
    Hostel_button = tk.Button(win, text="Hostel", command=lambda:sampletDeletionPage("Deletion","admissions"), width=20)
    Hostel_button.pack(pady=10)
    Department_button = tk.Button(win, text="Department", command=lambda:sampletDeletionPage("Deletion","departments"), width=20)
    Department_button.pack(pady=10)
    Programs_button = tk.Button(win, text="Programs", command=lambda:sampletDeletionPage("Deletion","programs"), width=20)
    Programs_button.pack(pady=10)
    Sessions_button = tk.Button(win, text="Sessions", command=lambda:sampletDeletionPage("Deletion","sessions"), width=20)
    Sessions_button.pack(pady=10)
    Student_info_button = tk.Button(win, text="Student_info", command=lambda:sampletDeletionPage("Deletion","student_info"), width=20)
    Student_info_button.pack(pady=10)
    Courses_button = tk.Button(win, text="Courses", command=lambda:sampletDeletionPage("Deletion","Courses"), width=20)
    Courses_button.pack(pady=10)
    Faculty_button = tk.Button(win, text="Faculty", command=lambda:sampletDeletionPage("Deletion","faculty"), width=20)
    Faculty_button.pack(pady=10)
    Exit_button = tk.Button(win, text="Exit", command=exit, width=20)
    Exit_button.pack(pady=10)


def sampletDeletionPage(title,table,*type):
    clearwindow()
    cur = database.cursor()
    win.title(title+" Page")
    cur.execute("SHOW COLUMNS from "+table)
    index=0
    tuple1 = []
    for i in cur.fetchall():
        tuple1.append(i[0])
    def deletefn(id):
        try:
            cur.execute("set foreign_key_checks=0")
            cur.execute("delete from "+table+" where Student_ID = "+str(id))
            database.commit()
        except Exception as e:
            print(e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="deleted Successfully")
            exit()
    def printpage():
        cur.execute("select * from "+table)
        for i in  cur.fetchall():
            print(i)
    frame = tk.Frame()
    cur.execute("select * from "+table)
    studentlist = cur.fetchall()
    tk.Label(frame, text=table+" list").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)
    index1 = 0
    for i in tuple1:
        tk.Label(frame, text=i).grid(row=1,column=index1,sticky="w")
        tk.Label(frame, text="--------------").grid(row=2,column=index1,sticky="w")
        index1+=1
    r=3
    for i in studentlist:
        indexj = 0
        for j in i:
            tk.Label(frame, text = i[indexj]).grid(row=r, column=indexj, sticky="w")
            indexj+=1
        if(len(type) == 0):
            tk.Button(frame,text= "Delete",command=lambda: deletefn(i[0]),width=20).grid(row=r,column=indexj,pady=10)
        frame.pack()
        r=r+1
    tk.Button(frame,text= "Exit",command= exit,width=20).grid(row=r,column=1,pady=30)
    tk.Button(frame,text= "Print",command= printpage,width=20).grid(row=r+1,column=1,pady=30)
    frame.pack()





def sampleInsertionPage(query,table):
    clearwindow()
    cur = database.cursor()
    win.title("Insertion Page")
    frame = tk.Frame()
    def change():
        c=0
        for i in list1:
            data[c] = i.get()
            c+=1
        try:
            cur.execute("set foreign_key_checks=0")
            cur.execute(query,data)
            database.commit()
        except Exception as e:
            print(e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="Inserted Successfully")
            exit()

    frame = tk.Frame()
    tk.Label(frame, text="Insert into "+table).grid(row=0, column=0, columnspan=2, sticky="news",pady=30)

    cur.execute("SHOW COLUMNS from "+table)
    list2 = cur.fetchall()
    list1 = list(range(0,len(list2)))
    data = list(range(0,len(list2)))
    index = 0
    for i in list2:
        tk.Label(frame, text=i[0]).grid(row=index+2, column=0)
        list1[index] = tk.Entry(frame)
        list1[index].grid(row=index+2, column=1, pady=10)
        index+=1
    
    tk.Button(frame, text="Insert", command=change).grid(row=index+2, column=0, pady=30)
    tk.Button(frame,text= "Exit",command= exit,width=20).grid(row=index+2,column=1, pady=30)

    frame.pack()



def AlterTablePage(table):
    query = "Alter table "+table+" "
    clearwindow()
    cur = database.cursor()
    win.title("Alter Table Page")
    frame = tk.Frame()
    tk.Label(frame, text="Alter column").grid(row=0, column=0, columnspan=2, sticky="news",pady=30)
    def add():
        try:
            cur.execute(query+"add column "+Column_name.get()+ " "+Column_type.get())
        except Exception as e:
            print(e)
            messagebox.showerror(title="Error", message=e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="Added Successfully")
            exit()
    def remove():
        try:
            cur.execute(query+"drop column "+Column_name.get())
        except Exception as e:
            print(e)
            messagebox.showerror(title="Error", message=e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="Removed Successfully")
            exit()
        
    tk.Label(frame, text="Column : ").grid(row=1, column=0)
    Column_name = tk.Entry(frame)
    Column_name.grid(row=1, column=1, pady=20)

    tk.Label(frame, text="Column type: ").grid(row=1, column=2)
    Column_type = tk.Entry(frame)
    Column_type.grid(row=1, column=3, pady=20)

    cur.execute("SHOW COLUMNS from "+table)
    list2 = cur.fetchall()
    index = 0
    for i in list2:
        tk.Label(frame, text=i[0]).grid(row=index+2, column=1)
        index+=1
    
    tk.Button(frame, text="Add column", command=add).grid(row=index+2, column=0, pady=30)
    tk.Button(frame, text="Drop column", command=remove).grid(row=index+2, column=1, pady=30)
    tk.Button(frame,text= "Exit",command= exit,width=20).grid(row=index+3,column=0,columnspan=2, pady=30)

    frame.pack()


