import tkinter as tk
from functools import partial
from tkinter import Scrollbar, messagebox,VERTICAL,RIGHT,Y,LEFT,BOTH


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
    win.title("Main Page")

    frame =scrollableframe()
    
    welcome_label = tk.Label(frame, text="Welcome to Marist College!", font=("Arial", 20))
    welcome_label.grid(row=1,column=1,pady=10,padx=500)

    admissions_button = tk.Button(frame, text="Admissions", command=AdmissionsPage, width=20)
    admissions_button.grid(row=2,column=1,pady=10,padx=500)

    programs_button = tk.Button(frame, text="Programs", command=lambda:sampletDeletionPage("Programs","Programs","main"), width=20)
    programs_button.grid(row=3,column=1,pady=10,padx=500)

    departments_button = tk.Button(frame, text="Departments", command=lambda:sampletDeletionPage("Department","Departments","main"), width=20)
    departments_button.grid(row=4,column=1,pady=10,padx=500)

    login_button = tk.Button(frame, text="Student Login", command=LoginPage, width=20)
    login_button.grid(row=5,column=1,pady=10,padx=500)

    hostel_button = tk.Button(frame, text="Hostel", command=show_hostel, width=20)
    hostel_button.grid(row=6,column=1,pady=10,padx=500)

    Change_Password_button = tk.Button(frame, text="Change Password", command=ChangeUserPassword, width=20)
    Change_Password_button.grid(row=7,column=1,pady=10,padx=500)

    aboutus_button = tk.Button(frame, text="About Us", command=aboutus, width=20)
    aboutus_button.grid(row=8,column=1,pady=10,padx=500) 

    if(admin == True):
        User_button = tk.Button(frame, text="Create New User", command=createuser, width=20)
        User_button.grid(row=10,column=1,pady=10,padx=500)
        Remove_button = tk.Button(frame, text="Remove User", command=RemoveUser, width=20)
        Remove_button.grid(row=11,column=1,pady=10,padx=500)     
        Insert_button = tk.Button(frame, text="Insertion", command=InsertionPage, width=20)
        Insert_button.grid(row=12,column=1,pady=10,padx=500)
        view_button = tk.Button(frame, text="View/search and Deletion", command=DeletionPage, width=20)
        view_button.grid(row=13,column=1,pady=10,padx=500)
        Alter_table = tk.Button(frame, text="Alter Table", command=AlterTable, width=20)
        Alter_table.grid(row=14,column=1,pady=10,padx=500)
        Change_normal_Password_button = tk.Button(frame, text="Change Normal Password", command=ChangeNormalUserPassword, width=20)
        Change_normal_Password_button.grid(row=15,column=1,pady=10,padx=500)
    
    Exit_button = tk.Button(frame, text="Exit", command=lambda: exit("window"), width=20)
    Exit_button.grid(row=16,column=1,pady=10,padx=500)
    


def aboutus():
    clearwindow()
    win.title("Change Password")

    frame = tk.Frame()
    
    tk.Label(frame, text="Pradeep Reddy Baireddy").grid(row=4, column=1, sticky="news",pady=(50,10))
    tk.Label(frame, text="Campus Id: 20150953").grid(row=5, column=1, sticky="news")

    tk.Label(frame, text="Pradeep Reddy Macha").grid(row=6, column=1, sticky="news",pady=(20,10))
    tk.Label(frame, text="Campus Id: 20150561").grid(row=7, column=1, sticky="news")

    tk.Label(frame, text="Bharatwaj Thota").grid(row=8, column=1, sticky="news",pady=(20,10))
    tk.Label(frame, text="Campus Id: 20150953").grid(row=9, column=1, sticky="news")

    tk.Label(frame, text="Prajakta kshirsagar").grid(row=10, column=1, sticky="news",pady=(20,10))
    tk.Label(frame, text="Campus Id: 20150953").grid(row=11, column=1, sticky="news")

    tk.Label(frame, text="Deepthi Niharika Gadepalli").grid(row=12, column=1, sticky="news",pady=(20,10))
    tk.Label(frame, text="Campus Id: 20150953").grid(row=13, column=1, sticky="news")

    tk.Label(frame, text="Chakradhar Reddy Marepally").grid(row=14, column=1, sticky="news",pady=(20,10))
    tk.Label(frame, text="Campus Id: 20150953").grid(row=15, column=1, sticky="news")
    


    tk.Button(frame,text= "Return",command= exit,width=20).grid(row=16,column=1,pady=30)

    frame.pack()

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
            messagebox.showerror(title="Error", message=e)
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
            messagebox.showerror(title="Error", message=e)
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
    win.title("Remove User")
    def Remove():
        try:
            if(username_entry != "root"):
                cur.execute("drop user if exists "+username_entry.get()+"@'localhost'")
                database.commit()
            else:
                exit()
                messagebox.showinfo(title="Error", message="Root user cannot be removed")
        except Exception as e:
            messagebox.showerror(title="Error", message=e)
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
            messagebox.showerror(title="Error", message=e)
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
    cur = database.cursor()
    cur.execute("SHOW tables")
            
    index = 0
    frame = scrollableframe()
    str = cur.fetchall()
    for i in str:
        temp = "INSERT INTO "+i[0]+" ("
        cur.execute("show columns from "+i[0])
        ind = 0
        for j in cur.fetchall():
            temp = temp + j[0] +","
            ind+=1
        temp = temp[:-1]+") values ("
        for m in range(0,ind):
            temp = temp +"%s," 
        temp = temp[:-1]+");"
        button = tk.Button(frame, text=i[0], command=partial(sampleInsertionPage,temp,i[0]), width=20)
        button.grid(row = index+3,column=1,padx=550,pady=10)
        index+=1
    Exit_button = tk.Button(frame, text="Exit", command=exit, width=20)
    Exit_button.grid(row = index+3,column=1,padx=550,pady=10)
    



def AlterTable():
    clearwindow() 
    cur = database.cursor()
    win.title("Main Page")
    cur.execute("SHOW tables")
    str = cur.fetchall()
    for i in str:
        button = tk.Button(win, text=i[0], command=partial(AlterTablePage,i[0]), width=20)
        button.pack(pady=10)



def DeletionPage():
    clearwindow() 
    cur = database.cursor()
    win.title("Main Page")
    cur.execute("SHOW tables")
    str = cur.fetchall()
    index = 0
    frame = scrollableframe()
    for i in str:
        Inserttstudent_button = tk.Button(frame, text=i[0], command=partial(sampletDeletionPage,"Deletion",i[0]), width=20)
        Inserttstudent_button.grid(row = index+3,column=1,padx=550,pady=10)
        index +=1
    Exit_button = tk.Button(frame, text="Exit", command=exit, width=20)
    Exit_button.grid(row = index+3,column=1,padx=550,pady=10)
    


def sampletDeletionPage(title,table,*type):
    clearwindow()
    cur = database.cursor()
    win.title(title+" Page")
    cur.execute("SHOW KEYS FROM "+table+" WHERE Key_name = 'PRIMARY';")
    primary = cur.fetchall()[0][4]
    cur.execute("SHOW COLUMNS from "+table)
    index=0
    tuple1 = []
    for i in cur.fetchall():
        tuple1.append(i[0])
    def deletefn(id):
        try:
            cur.execute("set foreign_key_checks=0")
            if(isinstance(primary, int)):
                cur.execute("delete from "+table+" where "+str(primary)+" = "+str(id))
            elif(isinstance(primary, str)):
                cur.execute("delete from "+table+" where "+str(primary)+" = '"+str(id)+"'")
            database.commit()
        except Exception as e:
            messagebox.showerror(title="Error", message=e)
            exit()
        else:
            messagebox.showinfo(title="Successful", message="deleted Successfully")
            sampletDeletionPage(title,table)
    def printpage():
        cur.execute("select * from "+table)
        for i in  cur.fetchall():
            print(i)
    frame = scrollableframe()
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
            btn = tk.Button(frame,text= "Delete",width=20)
            btn.grid(row=r,column=indexj,pady=10)
            btn["command"] = partial(deletefn,i[0])
        r=r+1
    
    tk.Button(frame,text= "Exit",command= exit,width=20).grid(row=r,column=1,pady=30)
    tk.Button(frame,text= "Print",command= printpage,width=20).grid(row=r,column=2,pady=30)
    





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
            messagebox.showerror(title="Error", message=e)
            
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

def scrollableframe():
    scroll_frame = tk.Frame()
    scroll_frame.pack(fill=BOTH,expand=1)

    canvas = tk.Canvas(scroll_frame)
    canvas.pack(side=LEFT,fill=BOTH,expand=1)

    scrollBar=Scrollbar(scroll_frame,orient=VERTICAL,command=canvas.yview)
    scrollBar.pack(side=RIGHT,fill=Y)

    canvas.configure(yscrollcommand=scrollBar.set)
    canvas.bind('<Configure>', lambda e:canvas.configure(scrollregion=canvas.bbox("all")))

    frame = tk.Frame(canvas)
    canvas.create_window((0,0),window=frame,anchor="nw")

    return frame