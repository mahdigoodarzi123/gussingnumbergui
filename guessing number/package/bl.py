from random import randrange
from tkinter import messagebox
from .dal import *


def init():
    res = create_table()

    if res[0] == "ERROR":
        return("ERROR" , res[1])
    else:
        return("SUCCESS" , "Done!")




def add(username , password , confirm_password):
    username = username.strip()
    password = password.strip()
    confirm_password = confirm_password.strip()


    err_list = list()


    if not username:
        err_list.append("username error")

    if not password:
        err_list.append("password error")

    if password != confirm_password:
        err_list.append("not match")


    if err_list:
        return("ERROR" , "/n".join(err_list))


    res = insert(username,password)
    if res[0] == "ERROR":
        return("ERROR",res[1])
    else:
        return("SUCCESS" , "Done!")




def get(username , password):
    username = username.strip()
    password = password.strip()
    err_list = list()

    if not username:
        err_list.append("username error")
    
    if not password:
        err_list.append("password error")
    

    if err_list:
        return  ("ERROR" , "\n".join(err_list))

    res = select(username,password)

    if res[0]=="ERROR":
        return("ERROR" , res[1])

    else:
        return("SUCCESS" , len(res[1])==1)




def random_maker(level):
    if level == 4 :
        random_number = randrange(1000 , 9999)
        return random_number

    
    elif level == 5 :
        random_number = randrange(10000 , 99999)
        return random_number


    elif level == 6 :
        random_number = randrange(100000 , 999999)
        return random_number
    
    
    elif level == 7 :
        random_number = randrange(1000000 , 9999999)
        return random_number
    

    elif level == 8:
        random_number = randrange(10000000 , 99999999)
        return random_number
    
    elif level == 9:
        random_number = randrange(100000000 , 999999999)
        return random_number
    
    elif level == 10:
        random_number = randrange(1000000000 , 9999999999)
        return random_number

    elif level == 11:
        random_number = randrange(10000000000 , 99999999999)
        return random_number



def number_split(level2):
    rand = random_maker(level2)
    # print(rand)
    digit = []
    for i in range(0,level2):
        rest = rand % 10
        digit.insert(0 , rest)
        rand = rand // 10

    return digit






# for bl
def check(number,first_entery , second_entry , third_entry , \
     forth_entry, fifth_entry , sixth_entery , \
     seventh_entry , eighth_entry , ninth_entry,\
    tenth_entry , eleventh_entry , name):
    entry1 = first_entery.get()
    entry2 = second_entry.get()
    entry3 = third_entry.get()
    entry4 = forth_entry.get()
    try:
        entry5 = fifth_entry.get()
    except:
        None
    try:
        entry6 = sixth_entery.get()
    except:
        None
    try:
        entry7 = seventh_entry.get()
    except:
        None
    try:
        entry8 = eighth_entry.get()
    except:
        None
    try:
        entry9 = ninth_entry.get()
    except:
        None
    try:
        entry10 = tenth_entry.get()
    except:
        None
    try:
        entry11 = eleventh_entry.get()
    except:
        None



    # print(number)
    # print(entry , entry2 , entry3 , entry4)
    firstdigit = str(number[0])
    seconddigit = str(number[1])
    thirddigit = str(number[2])
    fourthdigit = str(number[3])
    try:
        fifthdigit = str(number[4])
    except:
        None
    try:
        sixthdigit = str(number[5])
    except:
        None

    try:
        seventhdigit = str(number[6])
    except:
        None

    try:
        eighthdigit = str(number[7])
    except:
        None

    try:
        ninthdigit = str(number[8])
    except:
        None

    try:
        tenthdigit = str(number[9])
    except:
        None

    try:
        eleventhdigit = str(number[10])
    except:
        None
 
    error_list2 = []
    if firstdigit == entry1:
        error_list2.append("success")
        first_entery.config(state='disabled')
        # first_entery.config(bg = 'green') 
        
    else:
        error_list2.append("error")
    
    if seconddigit == entry2:
        error_list2.append("success")
        second_entry.config(state='disabled')
    else:
        error_list2.append("error")

    
    if thirddigit == entry3:
        error_list2.append("success")
        third_entry.config(state='disabled')
    else:
        error_list2.append("error")

    
    if fourthdigit == entry4:
        error_list2.append("success")
        forth_entry.config(state='disabled')
    else:
        error_list2.append("error")


    try:
        if fifthdigit == entry5:
            error_list2.append("success")
            fifth_entry.config(state='disabled')
        else:
            error_list2.append("error")
    except:
        None

    try:
        if sixthdigit == entry6:
            error_list2.append("success")
            sixth_entery.config(state='disabled')
        else:
            error_list2.append("error")
    except:
        None
    
    try:
        if seventhdigit == entry7:
            error_list2.append("success")
            seventh_entry.config(state='disabled')
        else:
            error_list2.append("error")
    except:
        None

    try:
        if eighthdigit == entry8:
            error_list2.append("success")
            eighth_entry.config(state='disabled')
        else:
            error_list2.append("error")
    except:
        None

    try:
        if ninthdigit == entry9:
            error_list2.append("success")
            ninth_entry.config(state='disabled')
        else:
            error_list2.append("error")
    except:
        None

    try:
        if tenthdigit == entry10:
            error_list2.append("success")
            tenth_entry.config(state='disabled')
        else:
            error_list2.append("error")
    except:
        None

    try:
        if eleventhdigit == entry11:
            error_list2.append("success")
            eleventh_entry.config(state='disabled')
        else:
            error_list2.append("error")
    except:
        None

#    print(error_list2)
    

    if error_list2[0] == "error":
        first_entery.delete(0, 'end')
    
    if error_list2[1] == "error":
        second_entry.delete(0, 'end')

    if error_list2[2] == "error":
        third_entry.delete(0, 'end')

    if error_list2[3] == "error":
        forth_entry.delete(0, 'end')


# for  level five
    try:
        if error_list2[4] == "error":
            fifth_entry.delete(0 , 'end')
    except:
        None

    try:
        if error_list2[5] == "error":
            sixth_entery.delete(0 , 'end')
    except:
        None
    
    try:
        if error_list2[6] == "error":
            seventh_entry.delete(0 , 'end')
    except:
        None

    try:
        if error_list2[7] == "error":
            eighth_entry.delete(0 , 'end')
    except:
        None

    try:
        if error_list2[8] == "error":
            ninth_entry.delete(0 , 'end')
    except:
        None

    try:
        if error_list2[9] == "error":
            tenth_entry.delete(0 , 'end')
    except:
        None

    try:
        if error_list2[10] == "error":
            eleventh_entry.delete(0 , 'end')
    except:
        None
    



    try:
        if error_list2[10]:
            if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and \
            error_list2[3] == "success" and \
                error_list2[4] == "success" and \
                    error_list2[5] == "success" and \
                        error_list2[6] == "success" and \
                            error_list2[7] == "success"and \
                                error_list2[8] == "success" and \
                                    error_list2[9] == "success" and \
                                        error_list2[10] == "success":
                messagebox.showinfo(None , "well done")
                name.destroy()
    except:
        try:
            if error_list2[9]:
                if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and \
                error_list2[3] == "success" and \
                    error_list2[4] == "success" and \
                        error_list2[5] == "success" and \
                            error_list2[6] == "success" and \
                                error_list2[7] == "success"and \
                                    error_list2[8] == "success" and \
                                        error_list2[9] == "success":
                    messagebox.showinfo(None , "well done")
                    name.destroy()

        except:
            try:
                if error_list2[8]:
                    if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and \
                        error_list2[3] == "success" and \
                            error_list2[4] == "success" and \
                                error_list2[5] == "success" and \
                                    error_list2[6] == "success" and \
                                        error_list2[7] == "success"and \
                                            error_list2[8] == "success":
                        messagebox.showinfo(None , "well done")
                        name.destroy()
            except:
                try:
                    if error_list2[7]:
                        if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and \
                            error_list2[3] == "success" and \
                                error_list2[4] == "success" and \
                                    error_list2[5] == "success" and \
                                        error_list2[6] == "success" and \
                                            error_list2[7] == "success":
                        
                            messagebox.showinfo(None , "well done")
                            name.destroy()

                except:
                    try:
                        if error_list2[6]:
                            if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and \
                                error_list2[3] == "success" and \
                                    error_list2[4] == "success" and \
                                        error_list2[5] == "success" and \
                                            error_list2[6] == "success":

                                messagebox.showinfo(None , "well done")
                                name.destroy()
    
                    except:
                        try:
                            if error_list2[5]:
                                if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and \
                                    error_list2[3] == "success" and \
                                        error_list2[4] == "success" and \
                                            error_list2[5] == "success":
                                    messagebox.showinfo(None , "well done")
                                    name.destroy()
    
    
                        except:
                            try:
                                if error_list2[4]:
                                    if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and error_list2[3] == "success" and error_list2[4] == "success":
                                        messagebox.showinfo(None , "well done")
                                        name.destroy()
                            except:
                                if error_list2[0] == "success" and error_list2[1] == "success" and error_list2[2] == "success" and error_list2[3] == "success":
                                    messagebox.showinfo(None , "well done")
                                    name.destroy()




