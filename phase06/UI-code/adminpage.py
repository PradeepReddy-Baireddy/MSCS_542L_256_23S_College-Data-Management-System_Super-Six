import tkinter as tk
from tkinter import PhotoImage, messagebox
import mysql.connector
from MainPage import OpenMain


def AdminLogin():
    win = tk.Tk()
    win.title("User")
    win.geometry("400x400")
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
            
    frame = tk.Frame()
    logo = PhotoImage(file="Marist_Seal.png")
    welcomeimg = PhotoImage(file="NewImg.png")
    
    tk.Label(frame, image=welcomeimg).grid(row=0, column=1, sticky="news",pady=10)
    tk.Label(frame, image=logo).grid(row=0, column=4, columnspan=4, sticky="news",padx=100,pady=80)

    tk.Label(frame, text="Username").grid(row=2, column=0)
    username_entry = tk.Entry(frame)
    username_entry.grid(row=2, column=1, pady=20)

    tk.Label(frame, text="Password").grid(row=3, column=0)
    password_entry = tk.Entry(frame)
    password_entry.grid(row=3, column=1, pady=20)

    tk.Button(frame, text="Login", command=lambda: login(win)).grid(row=4, column=0, columnspan=2, pady=30)

    frame.pack()
    win.mainloop()




AdminLogin()
