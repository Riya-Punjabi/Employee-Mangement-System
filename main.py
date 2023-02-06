import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

#login part
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='riya' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct credentials')

#to open the window tab
window=Tk()

window.geometry('1280x700+0+0')
window.title("Login ")

window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

#creating username and password
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',
                   activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()