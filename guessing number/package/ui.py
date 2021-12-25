from abc import abstractclassmethod
from tkinter import *
from tkinter import font
from tkinter.messagebox import *
from .bl import *


def login_onclick(form , username_entry , password_entry):
    username = username_entry.get()
    password = password_entry.get()
    
    res2 = get(username , password)

    if res2[0]=="ERROR":
        username_entry.delete(0 , END)
        password_entry.delete(0 , END)
        showerror("ERROR" , res2[1])


    elif res2[1]:
        # form.destroy()
        main_form()

        

    elif not res2[1]:
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        showerror("ERROR" , "USERNAME OR PASSWORD ERROR")






def register_onclick(form , username_entry , password_entry , confirm_password_entry):
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()


    res = add(username , password , confirm_password)

    if res[0] == "ERROR":
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        confirm_password_entry.delete(0,END)
        showerror("ERROR",res[1])


    else:
        showinfo("Success",res[1])
        form.destroy()
        login_form()

def load_page():
    res = init()
    if res[0] == "ERROR":
        showerror("ERROR" ,res[1])



def login_to_register(form):
    form.destroy()
    register_form()


def register_to_login(form):
    form.destroy()
    login_form()




def login_form():
    login = Tk()
    login.title("login form")
    login.geometry("350x350")
    login.configure(bg="white")
    



    body = Frame(
        master=login,
        bg="white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)
    
# password label   
    Label(
        master=body,
        text="username:",
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        anchor=W
    ).pack(padx=(30,30) , pady=(70,0))



# username entry
    username_entry = Entry(
        master=body,
        bg="white",
        fg="gray",
        font=("Tahoma",14,"normal")
    )
    username_entry.pack()



# password label
    Label(
        master=body,
        text="password:",
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        anchor=W
    ).pack(padx=(30,30) , pady=(60,0))



# password entry
    password_entry = Entry(
        master=body,
        bg="white",
        fg="gray",
        font=("Tahoma",14,"normal")
    )
    password_entry.pack(pady=(0,15))


    
# login button
    Button(
        master=body,
        text="Login!!!",
        bg="#28a745", 
        fg="white",
        font= ("Tahoma",10,"bold"),
        pady= 5,
        command= lambda: login_onclick(login,username_entry,password_entry)
    ).pack(side=TOP,fill=X,pady=(0,3),padx=(30,30))

    

# register button
    Button(
        master=body,
        text="register",
        bg="red",
        fg="white",
        font=("Tahoma",10,"bold"),
        pady=5,
        command= lambda : login_to_register(login)
    ).pack(side=TOP,fill=X,pady=(0,3),padx=(30,30))




    
    login.mainloop()


def register_form():
    register = Tk()
    register.title("register form")
    register.geometry("450x450")
    register.resizable(width=False , height=False)
    register.configure(bg="white")

    body = Frame(
        master=register,
        bg="white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)



# username region
    Label (
        master=body,
        text="username:",
        bg="white", 
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        anchor=W
    ).pack(side=TOP,fill=X,pady=(50,0),padx=(30,30))



#username entry
    username_entry = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 14 , "normal")
    )
    username_entry.pack(side=TOP,fill=X,pady=(0,10),padx=(30,30))



#password region
    Label (
        master=body,
        text="password:",
        bg="white", 
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        anchor=W
    ).pack(side=TOP,fill=X,pady=(20,0),padx=(30,30))



# password entry
    password_entry = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 14 , "normal")
    )
    password_entry.pack(side=TOP,fill=X,pady=(0,10),padx=(30,30))




# confirm password region
    Label (
        master=body,
        text="confirm password:",
        bg="white", 
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        anchor=W
    ).pack(side=TOP,fill=X,pady=(20,0),padx=(30,30))



# confirm password entry
    confirm_password_entry = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 14 , "normal")
    )
    confirm_password_entry.pack(side=TOP,fill=X,pady=(0,10),padx=(30,30))



#region BUTTON
    Button(
        master=body,
        text="register!!!",
        bg="green", 
        fg="white",
        font= ("Tahoma",10,"bold"),
        pady= 5,
        command= lambda : register_onclick(register , username_entry , password_entry , confirm_password_entry)
    ).pack(side=TOP,fill=X,pady=(0,3),padx=(30,30))
    
#back button
    Button(
        master=body,
        text="BACK!!!",
        bg="red", 
        fg="white",
        font= ("Tahoma",10,"bold"),
        pady= 5,
        command= lambda : register_to_login(register)
    ).pack(side=TOP,fill=X,pady=(0,3),padx=(30,30))
    #endregion

    
    
    register.mainloop()



#forth one
def four():
    main = Tk()
    main.title("forth digit number")
    main.resizable(0,0)
    main.geometry("350x250")
    main.configure(bg="white")

    #this is a test
    lev= 4
    #this is a test
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1 = Entry(
        master=body,
        bg="white",
        fg="black",
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

    e2 = Entry(
        master=body,
        bg="white",
        fg="black",
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)

    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)


    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, None , None , None , None, None, None, None , main)
    ).pack(side=TOP , pady=50)


    main.mainloop()
    


################################################################

#fifth one
def five():
    main = Tk()
    main.title("forth digit number")
    # main.resizable(0,0)
    main.geometry("415x250")
    main.configure(bg="white")


    lev= 5
    #this is a test
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

#second entry
    e2 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)



#third entry
    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


#fifth entry
    e5 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e5.place(width=50 , height=50, x=355 , y=60)


#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, e5 , None , None , None, None, None, None , main)
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)

    main.mainloop()

#sixth one
def six():
    main = Tk()
    main.title("forth digit number")
    main.resizable(0,0)
    main.geometry("500x250")
    main.configure(bg="white")


    lev = 6
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1= Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

#second entry
    e2 =Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)



#third entry
    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


#fifth entry
    e5 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e5.place(width=50 , height=50, x=355 , y=60)



#sixth entry
    e6 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e6.place(width=50 , height=50, x=440 , y=60)


#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, e5 , e6 , None , None, None, None, None , main)
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)






    main.mainloop()


def seven():
    main = Tk()
    main.title("forth digit number")
    main.resizable(0,0)
    main.geometry("600x250")
    main.configure(bg="white")


    lev = 7
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1= Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

#second entry
    e2 =Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)



#third entry
    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


#fifth entry
    e5 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e5.place(width=50 , height=50, x=355 , y=60)



#sixth entry
    e6 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e6.place(width=50 , height=50, x=440 , y=60)


    e7 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e7.place(width=50 , height=50, x=525 , y=60)


#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, e5 , e6 , e7 , None, None, None, None , main)
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)






    main.mainloop()


def eight():
    main = Tk()
    main.title("forth digit number")
    main.resizable(0,0)
    main.geometry("700x250")
    main.configure(bg="white")


    lev = 8
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1= Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

#second entry
    e2 =Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)



#third entry
    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


#fifth entry
    e5 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e5.place(width=50 , height=50, x=355 , y=60)



#sixth entry
    e6 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e6.place(width=50 , height=50, x=440 , y=60)


    e7 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e7.place(width=50 , height=50, x=525 , y=60)


    e8 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e8.place(width=50 , height=50, x=610 , y=60)


#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, e5 , e6 , e7 , e8, None, None, None , main)
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)






    main.mainloop()



def ninth():
    main = Tk()
    main.title("forth digit number")
    # main.resizable(0,0)
    main.geometry("800x250")
    main.configure(bg="white")


    lev = 9
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1= Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

#second entry
    e2 =Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)



#third entry
    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


#fifth entry
    e5 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e5.place(width=50 , height=50, x=355 , y=60)



#sixth entry
    e6 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e6.place(width=50 , height=50, x=440 , y=60)


    e7 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e7.place(width=50 , height=50, x=525 , y=60)


    e8 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e8.place(width=50 , height=50, x=610 , y=60)

    e9 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e9.place(width=50 , height=50, x=695 , y=60)

#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, e5 , e6 , e7 , e8 , e9 , None , None , main)
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)






    main.mainloop()


def tenth():
    main = Tk()
    main.title("forth digit number")
    main.resizable(0,0)
    main.geometry("850x250")
    main.configure(bg="white")


    lev = 10
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1= Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

#second entry
    e2 =Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)



#third entry
    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


#fifth entry
    e5 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e5.place(width=50 , height=50, x=355 , y=60)



#sixth entry
    e6 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e6.place(width=50 , height=50, x=440 , y=60)


    e7 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e7.place(width=50 , height=50, x=525 , y=60)


    e8 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e8.place(width=50 , height=50, x=610 , y=60)

    e9 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e9.place(width=50 , height=50, x=695 , y=60)

    e10 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e10.place(width=50 , height=50, x=780 , y=60)
    
#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, e5 , e6 , e7 , e8 , e9 , e10 , None , main)
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)






    main.mainloop()



def eleventh():
    main = Tk()
    main.title("forth digit number")
    main.resizable(0,0)
    main.geometry("950x250")
    main.configure(bg="white")


    lev = 11
    numb = number_split(lev)



# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    e1= Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e1.place(width=50 , height=50, x=15 , y=60)

#second entry
    e2 =Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e2.place(width=50 , height=50, x=100 , y=60)



#third entry
    e3 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e3.place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    e4 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e4.place(width=50 , height=50, x=270 , y=60)


#fifth entry
    e5 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e5.place(width=50 , height=50, x=355 , y=60)



#sixth entry
    e6 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e6.place(width=50 , height=50, x=440 , y=60)


    e7 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e7.place(width=50 , height=50, x=525 , y=60)


    e8 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e8.place(width=50 , height=50, x=610 , y=60)

    e9 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e9.place(width=50 , height=50, x=695 , y=60)

    e10 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e10.place(width=50 , height=50, x=780 , y=60)

    e11 = Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    )
    e11.place(width=50 , height=50, x=865 , y=60)
    
#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20,
        command= lambda: check(numb, e1 , e2 , e3 , e4, e5 , e6 , e7 , e8 , e9 , e10 , e11 , main)
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)






    main.mainloop()




# body
    body = Frame(
        master= main,
        bg = "white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)

#footer
    footer = Frame(
        master=main,
        bg="white",
        width=5
    )
    footer.pack(fill=BOTH,expand=1)
    footer.propagate(0)

#first entry
    Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    ).place(width=50 , height=50, x=15 , y=60)

#second entry
    Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    ).place(width=50 , height=50, x=100 , y=60)



#third entry
    Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    ).place(width=50 , height=50, x=185 , y=60)
    
#forth entry
    Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    ).place(width=50 , height=50, x=270 , y=60)


#fifth entry
    Entry(
        master=body,
        bg="white",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        justify='center'
    ).place(width=50 , height=50, x=355 , y=60)


#check button
    Button(
        master=footer,
        text="check",
        bg="green",
        fg="black",
        font=("Tahoma" , 10 , "bold"),
        padx=45,
        pady=20
    ).pack(side=TOP , pady=50)
# .place(width=20 , height=20 , x=170 , y=50)






    main.mainloop()

##############################################################



def main_form():
    management = Tk()
    management.title("main page")
    management.resizable(0,0)
    management.geometry("514x574")
    management.configure(bg="white")


# body region
    body = Frame(
        master=management,
        bg="white"
    )
    body.pack(fill=BOTH , expand=True)
    body.propagate(0)


# label region for text
    Label(
        master=body, 
        text="levels : ", 
        bg="white", 
        fg="black",
        font= ("Tahoma",10,"bold"),
        anchor=W
    ).pack(side=TOP,fill=BOTH)


# button 4
    Button(
        master=body , 
        text="4",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : four()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))

# button 5
    Button(
        master=body , 
        text="5",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : five()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))

# button 6
    Button(
        master=body , 
        text="6",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : six()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))

# button 7
    Button(
        master=body , 
        text="7",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : seven()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))

# button 8
    Button(
        master=body , 
        text="8",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : eight()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))

# button 9
    Button(
        master=body , 
        text="9",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : ninth()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))
# button 10
    Button(
        master=body , 
        text="10",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : tenth()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))


# button 11
    Button(
        master=body , 
        text="11",
        bg="gray",
        fg="black",
        padx=25,
        pady=20,
        command= lambda : eleventh()
    ).pack(side=TOP , fill=BOTH,pady=(0,5))

    management.mainloop()


load_page()