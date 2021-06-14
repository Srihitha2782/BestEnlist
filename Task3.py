#importing library
from tkinter import *
from tkinter import ttk
window = Tk()
#window title
window.title("Employee Registration Form")
#window geometry
window.geometry("300x300")
#window colour
window.configure(background="black");
#below nine fields are declaration
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "LastName").grid(row =1,column=0)
Address = Label(window ,text = "Address").grid(row =2,column=0)
City = Label(window ,text = "City").grid(row =3,column=0)
Pincode = Label(window ,text = "Pincode").grid(row =4,column=0)
State = Label(window ,text = "State").grid(row =5,column=0)
Country = Label(window ,text = "Country").grid(row =6,column=0)
Email = Label(window ,text = "Email id").grid(row =7,column=0)
Mobile = Label(window ,text = "Contact Number").grid(row =8,column=0)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Address1 = Entry(window).grid(row = 2,column = 1)
City1 = Entry(window).grid(row = 3,column = 1)
Pincode1 = Entry(window).grid(row = 4,column = 1)
State1 = Entry(window).grid(row = 5,column = 1)
Country1 = Entry(window).grid(row = 6,column = 1)
Email1= Entry(window).grid(row = 7,column = 1)
Mobile1 = Entry(window).grid(row = 8,column = 1)

#function declaration
def clicked():
    res = "Welcome to" + txt.get()
    lbl.configure (text = res)
btn = ttk.Button(window,text="Submit").grid(row=9,column=0)
window.mainloop()