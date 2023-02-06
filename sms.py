from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql

# for exit button function
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
# end exit button function    
    
# for add data button function
def Add_data():
#user add in to the mysql database also    
    def Add_user():
        if  nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or  genderEntry.get()=='' or SocialMediaEntry.get()=='' or CrimeRecordEntry.get()=='':
          messagebox.showerror('Error','All Feilds are required',parent=add_window)
        else:
            query='insert into User values(%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),
                                    genderEntry.get(),SocialMediaEntry.get(),CrimeRecordEntry.get(),date,currenttime))
            con.commit()  
            result=messagebox.askyesno('Confirm','Data added successfuly. Do you want to clean the form?',parent = add_window)
            if result:
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                genderEntry.delete(0,END)
                SocialMediaEntry.delete(0,END)
                CrimeRecordEntry.delete(0,END)
            else:
                pass
            query='select *from User'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            userTable.delete(*userTable.get_children())
            for data in fetched_data:
               userTable.insert('',END,values=data)
# for data added in to the preview               
    add_window=Toplevel()
    add_window.resizable(False , False)
#for adding window size and position
    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)
  
    phoneLabel = Label(add_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    SocialMediaLabel = Label(add_window, text='SocialMedia', font=('times new roman', 20, 'bold'))
    SocialMediaLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    SocialMediaEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    SocialMediaEntry.grid(row=6, column=1, pady=15, padx=10)

    CrimeRecordLabel = Label(add_window, text='Crime-Record', font=('times new roman', 20, 'bold'))
    CrimeRecordLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    CrimeRecordEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    CrimeRecordEntry.grid(row=6, column=1, pady=15, padx=10)

    add_button = ttk.Button(add_window, text='Add data',command=Add_user)
    add_button.grid(row=7, columnspan=2, pady=15)
#end add function    

# for search button function
def search_user():
#user search query perform in to the mysql database also     
    def search_data():
         query='select * from User where  name=%s or email=%s or mobile=%s or  gender=%s or SocialMedia=%s or CrimeRecord=%s'
         mycursor.execute(query,(nameEntry.get(),emailEntry.get(),phoneEntry.get(),genderEntry.get(),SocialMediaEntry.get(),CrimeRecordEntry.get()))
         userTable.delete(*userTable.get_children())
         fetched_data=mycursor.fetchall()
         for data in fetched_data:
            userTable.insert('',END,values=data)
        
    search_window=Toplevel()
    search_window.resizable(False , False)
    search_window.title('Search Student')
    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)
  
    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    SocialMediaLabel = Label(search_window, text='SocialMedia', font=('times new roman', 20, 'bold'))
    SocialMediaLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    SocialMediaEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    SocialMediaEntry.grid(row=6, column=1, pady=15, padx=10)

    CrimeRecordLabel = Label(search_window, text='Crime-Record', font=('times new roman', 20, 'bold'))
    CrimeRecordLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    CrimeRecordEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    CrimeRecordEntry.grid(row=6, column=1, pady=15, padx=10)

    search_button = ttk.Button(search_window, text='Search data',command=search_data)
    search_button.grid(row=7, columnspan=2, pady=15)
#end search function    

#user delect in to the mysql database as well as in to preview
#start delect function
def delete_user():
    indexing=userTable.focus()
    print(indexing)
    content=userTable.item(indexing)
    content_name=content['values'][0]
    query='delete from User where name=%s'
    mycursor.execute(query,content_name)
    con.commit()
    messagebox.showinfo('Deleted',f'name {content_name} is deleted succesfully')
    query='select * from User'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    userTable.delete(*userTable.get_children())
    for data in fetched_data:
        userTable.insert('',END,values=data) 
#end delect function        

#user update in to the mysql database as well as in to preview
def update_user():
    def update_data():
        query='update User set name=%s,mobile=%s,email=%s,gender=%s,SocialMedia=%s,CrimeRecord=%s,date=%s,time=%s where name=%s'
        mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),
                            genderEntry.get(),SocialMediaEntry.get(),CrimeRecordEntry.get(),date,currenttime))
        con.commit()
        messagebox.showinfo('Success',f'Id {nameEntry.get()} is modified successfully',parent=update_window)
        update_window.destroy()
        show_data()

    update_window=Toplevel()
    update_window.resizable(False , False)
    update_window.title('Update Student')
    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)
    phoneLabel = Label(update_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    SocialMediaLabel = Label(update_window, text='SocialMedia', font=('times new roman', 20, 'bold'))
    SocialMediaLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    SocialMediaEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    SocialMediaEntry.grid(row=6, column=1, pady=15, padx=10)

    CrimeRecordLabel = Label(update_window, text='Crime-Record', font=('times new roman', 20, 'bold'))
    CrimeRecordLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    CrimeRecordEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    CrimeRecordEntry.grid(row=6, column=1, pady=15, padx=10)

    update_button = ttk.Button(update_window, text='Update data',command=update_data)
    update_button.grid(row=7, columnspan=2, pady=15)

    indexing = userTable.focus()

    content = userTable.item(indexing)
    listdata = content['values']
    nameEntry.insert(0, listdata[0])
    phoneEntry.insert(0, listdata[1])
    emailEntry.insert(0, listdata[2])
    genderEntry.insert(0, listdata[3])
    SocialMediaEntry.insert(0, listdata[4])
    CrimeRecordEntry.insert(0 , listdata[5])
#end update function    

def show_data():
    query = 'select * from User'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    userTable.delete(*userTable.get_children())
    for data in fetched_data:
        userTable.insert('', END, values=data) 

def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost', user='root', password='Riya@258') #my database hostname , username and password
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table User( name varchar(30) not null , mobile varchar(10) not null,email varchar(30) not null,' \
                   'gender varchar(20),SocialMedia varchar(20),date varchar(50), time varchar(50),CrimeRecord varchar(5) not null)'
            mycursor.execute(query)
        except:
            query='use userdata'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        adddataButton.config(state=NORMAL)
        searchuserButton.config(state=NORMAL)
        updateuserButton.config(state=NORMAL)
        showuserButton.config(state=NORMAL)
        deleteuserButton.config(state=NORMAL)    

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)
#for creating slider
count=0
text=''
def slider():
    global text,count
    # text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)
#for creating clock
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

#prvide the theme to gui part    
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Uses data')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s='Data' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

#GUI part
connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

adddataButton=ttk.Button(leftFrame,text='Add Data',width=25,state=DISABLED,command=Add_data)
adddataButton.grid(row=1,column=0,pady=20)

searchuserButton=ttk.Button(leftFrame,text='Search User',width=25,state=DISABLED,command=search_user)
searchuserButton.grid(row=2,column=0,pady=20)

deleteuserButton=ttk.Button(leftFrame,text='Delete User',width=25,state=DISABLED,command=delete_user)
deleteuserButton.grid(row=3,column=0,pady=20)

updateuserButton=ttk.Button(leftFrame,text='Update User',width=25,state=DISABLED,command=update_user)
updateuserButton.grid(row=4,column=0,pady=20)

showuserButton=ttk.Button(leftFrame,text='Show User',width=25,state=DISABLED,command=show_data)
showuserButton.grid(row=5,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=6,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

userTable=ttk.Treeview(rightFrame,columns=('Name','Mobile','Email','Gender','Social Media','Crime Record'),
                                 xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=userTable.xview)
scrollBarY.config(command=userTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

userTable.pack(expand=1,fill=BOTH)     


userTable.heading('Name',text='Name')
userTable.heading('Mobile',text='Mobile No')
userTable.heading('Email',text='Email Address')
userTable.heading('Gender',text='Gender')
userTable.heading('Social Media',text='Social Media')
userTable.heading('Crime Record',text='Crime Record')

userTable.column('Name',width=200,anchor=CENTER)
userTable.column('Mobile',width=200,anchor=CENTER)
userTable.column('Email',width=200,anchor=CENTER)
userTable.column('Gender',width=100,anchor=CENTER)
userTable.column('Social Media',width=200,anchor=CENTER)
userTable.column('Crime Record',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='black')

userTable.config(show='headings')

root.mainloop()
