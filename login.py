import tkinter
import sqlite3
from tkinter import messagebox
from  home import home_page
from databases import database, books

window = tkinter.Tk()

window.geometry("500x400")
window.title("E-just's E-library")

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(7, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(7, weight=1)

# conn = sqlite3.connect('credentials.db')

label = tkinter.Label(window, text="Welcome to E-just's E-library").grid(row=1, column=1, columnspan=2, ipadx=10, ipady=20)

name = tkinter.Label(window, text="Name").grid(row=2, column=1, sticky="W", ipadx=10, ipady=10)
name_entry = tkinter.Entry(window)
name_entry.grid(row=2, column=2)

password = tkinter.Label(window, text="Password").grid(row=3, column=1, sticky="W", ipadx=10, ipady=10)
password_entry = tkinter.Entry(window)
password_entry.grid(row=3, column=2)

def sign_up():
    sign_up = tkinter.Tk()

    sign_up.geometry("500x400")
    sign_up.title("Sign up")

    sign_up.grid_rowconfigure(0, weight=1)
    sign_up.grid_rowconfigure(7, weight=1)
    sign_up.grid_columnconfigure(0, weight=1)
    sign_up.grid_columnconfigure(7, weight=1)

    name = tkinter.Label(sign_up, text="Name").grid(row=2, column=1, sticky="W", ipadx=10, ipady=10)
    name_entry = tkinter.Entry(sign_up)
    name_entry.grid(row=2, column=2)

    password = tkinter.Label(sign_up, text="Email").grid(row=3, column=1, sticky="W", ipadx=10, ipady=10)
    password_entry = tkinter.Entry(sign_up)
    password_entry.grid(row=3, column=2)

    name = tkinter.Label(sign_up, text="Enter Password").grid(row=4, column=1, sticky="W", ipadx=10, ipady=10)
    name_entry = tkinter.Entry(sign_up)
    name_entry.grid(row=4, column=2)

    password = tkinter.Label(sign_up, text="Re-enter Password").grid(row=5, column=1, sticky="W", ipadx=10, ipady=10)
    password_entry = tkinter.Entry(sign_up)
    password_entry.grid(row=5, column=2)
    
    tkinter.Button(sign_up, text="Sign up", command=lambda:sign_up.destroy()).grid(row=6, column=1, columnspan=2)

    
def get_input():
    get_name = name_entry.get()
    get_password = password_entry.get()

    global params
    params = [get_name, get_password]
    
    if(get_name not in database):
        tkinter.Label(window, text="You're not a member, sign up instead!").grid(row=5, column=1, columnspan=2)
        signup_button = tkinter.Button(window, text="Sign up", command=sign_up).grid(row=6, column=1, columnspan=2)
    else:
        if(database[get_name] == get_password):
            window.destroy()
            home_page()
        else:
            messagebox.showerror('Error', 'The Password doesn\'t match the username!') 

login_button = tkinter.Button(window, text="Login", command=get_input).grid(row=4, column=1, columnspan=2)

window.resizable(False, False)
window.mainloop()
