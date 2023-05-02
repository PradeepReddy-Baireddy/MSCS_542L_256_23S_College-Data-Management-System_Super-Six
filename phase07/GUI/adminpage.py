import tkinter as tk
from tkinter import PhotoImage, Scrollbar, messagebox,VERTICAL,RIGHT,Y,LEFT,BOTH
import mysql.connector
from MainPage import OpenMain


def AdminLogin():
    win = tk.Tk()
    win.title("User")
    win.state('zoomed')
    def login(win):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user= username_entry.get(),
                passwd = password_entry.get(),
                database="super_six"
                )
                
        except:
            messagebox.showerror(title="Error", message="Incorrect Username or Password")
        else:
            list = win.pack_slaves()
            for i in list:
                i.destroy()
            OpenMain(win,db)
            messagebox.showinfo(title="Successfully loggedIn", message="You have successfully logged in.")
            
            
    
    logo = PhotoImage(file="Marist_Seal.png")
    welcomeimg = PhotoImage(file="NewImg.png")

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


    tk.Label(frame, image=welcomeimg).grid(row=0, column=4,padx=(400,200),pady=10)
    tk.Label(frame, image=logo).grid(row=0, column=5, sticky="w",pady=80)

    tk.Label(frame, text="Username").grid(row=2, column=4, columnspan=2)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=3, column=4, columnspan=2, pady=20)

    tk.Label(frame, text="Password").grid(row=4, column=4, columnspan=2)
    password_entry = tk.Entry(frame)
    password_entry.grid(row=5, column=4, pady=20, columnspan=2)

    
    tk.Button(frame, text="Login", command=lambda: login(win)).grid(row=6, column=4, columnspan=2, pady=30)

    win.mainloop()

AdminLogin()
