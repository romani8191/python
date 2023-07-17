from tkinter import *
import tkinter.messagebox as tmsg
import mysql.connector
import os
from PIL import ImageTk, Image

# def insert():
#     a=n.get(),
#     b=acc.get(),
#     c=bal.get()
#
#     db = mysql.connector.connect(
#         host="localhost",
#         username="root",
#         password="",
#         database="starGirl"
#     )
#
#     i = db.cursor()
#     i.execute("insert into db values(%s,%s,%s)"(a,b,c))
#     i.execute("commit")
#


bank = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="starGirl"
)

print("database created")
mycursor = bank.cursor()

mycursor.execute('drop table if exists bank')
print('bank table dropped')

mycursor.execute('create table bank(AccountNo int primary key, name varchar(25),balance int(50))')
print('table created')

sql = 'insert into bank (AccountNo ,name, balance) values(%s,%s,%s)'
val = [
    (1001, "Romani", 300000),
    (1002, "Prerna", 200000),
    (1003, "Nitesh", 100000)
]

mycursor.executemany(sql, val)
bank.commit()
print(mycursor.rowcount, "Record was inserted")

mycursor.execute("select * from bank")
result = mycursor.fetchall()
for records in result:
    print(records)




def OpAcc():

    Label(text="Please enter your name: ", bg="yellow", fg="orange").grid(row=3, column=1)
    n = Entry().grid(row=3, column=2)
    Label(text="enter the account no. : ", bg="yellow", fg="orange").grid(row=4, column=1)
    acc = Entry().grid(row=4, column=2)
    Label(text="Enter the balance ", bg="yellow", fg="orange").grid(row=5, column=1)
    bal = Entry().grid(row=5, column=2)

    AccountNo = acc.get()
    name = n.get()
    balance = bal.get()

    data = (AccountNo, name, balance)
    sql = "insert into bank values(%s, %s, %s)"
    mycursor = bank.cursor()
    mycursor.execute(sql, data)
    bank.commit()
    tmsg.showinfo("Your Account has been created :)")
    tmsg.showinfo("Data has been entered :) ")



def withdraw():
    amount = int(input("Enter the amount u want to deposit : "))
    acc = int(input("Enter the account no. : "))
    a = "select balance from bank where AccountNo=%s"
    data = (acc,)
    mycursor = bank.cursor()
    mycursor.execute(a, data)
    result = mycursor.fetchone()
    total = result[0] - amount
    sql = "update bank set balance=%s where AccountNo=%s"
    d = (total, acc)
    mycursor.execute(sql, d)
    bank.commit()
    login()


def search():
    ac = input("Please enter the account no : ")
    a = "select * from bank where AccountNo=%s"
    data = (ac,)
    c = bank.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    print(f"The info of the required account is : {myresult}")
    login()


#
def ListAcc():
    mycursor.execute("select * from bank")
    result = mycursor.fetchall()
    for records in result:
        print(records)
    login()

def depo():
    global amount
    global deposit_notif
    global current_balance_label

    deposit_screen = Toplevel(root)
    deposit_screen.title("Deposit")



    amount = int(input("Enter the amount u want to deposit : "))
    acc = int(input("Enter the account no. : "))
    a = "select balance from bank where AccountNo=%s"
    data = (acc,)
    mycursor = bank.cursor()
    mycursor.execute(a, data)
    result = mycursor.fetchone()
    total = result[0] + amount
    sql = "update bank set balance=%s where AccountNo=%s"
    d = (total, acc)
    mycursor.execute(sql, d)
    bank.commit()

    Label(deposit_screen, text="Deposit", font="Times 12 bold italic").grid(row=0, sticky=N, pady=10)
    current_balance_label = Label(deposit_screen, text=f"Current Balance: {a}", font="calibri 10 bold").grid(row=1,
                                                                                                             sticky=W)
    Label(deposit_screen, text="Amount: ", font="Times 12 bold italic").grid(row=2, sticky=W, pady=10)
    deposit_notif(font="Times 12 bold italic").grid(row=4, sticky=N, pady=5)
    Entry(deposit_screen, textvariable=amount).grid(row=2, column=1)
    Button(deposit_screen, text="finish").grid(row=3, sticky=N, pady=5)

    login()

def login():
    all_accounts=os.listdir()
    log_user=log_name.get()
    log_pass=magicword.get()

    for name in all_accounts:
        if name ==log_user:
            file=open(name,"r")
            data = file.read()
            data=data.split("\n")
            password=data[2]

            if log_pass==password:
                # login.destroy()
                account=Toplevel(root)
                account.geometry("400x200")
                account.title("Dashboard")
                # labels
                Label(account, text="Account Dashboard", font="Times 10 bold italic").grid(row=0,sticky=N,pady=10)
                Label(account, text=f"Welcome {name}", font="Times 10 bold italic").grid(row=1,sticky=N,pady=10)

                bank = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="",
                    database="starGirl"
                )



                mymenue = Menu(account)
                n = StringVar()
                acc = StringVar()
                bal = StringVar()
                mymenue.add_command(label="New Account", command=OpAcc)
                mymenue.add_command(label="List Account", command=ListAcc)
                mymenue.add_command(label="Search", command=search)
                mymenue.add_command(label="Deposit", command=depo)
                mymenue.add_command(label="Withdraw", command=withdraw)
                mymenue.add_command(label="Exit", command=quit)

                account.config(menu=mymenue)



            else:
                log_notif.config(text="Please enter correct password", fg="red")
                return
    log_notif.config(text="Account not found", fg="red")




def finish():

    name=temp_name.get()
    user=temp_user.get()
    password=temp_password.get()
    email=temp_email.get()
    phone=temp_phone.get()
    all_accounts=os.listdir()

    if name==""  or user==" " or password==" " or email==" " or phone==" ":
        notif.config(text="Please enter all the values ", fg="red")
        return
    for name_check in all_accounts:
        if name==name_check:
            notif.config(text="Account already exists", fg="red")
            return
        else :
            new_file=open(name,"w")
            new_file.write(name+"\n")
            new_file.write(user+"\n")
            new_file.write(password+"\n")
            new_file.write(email+"\n")
            new_file.write(phone+"\n")
            new_file.write('0')
            new_file.close()
            notif.config(text="good to go :) ", fg="green")


def SIGNUP():
    signup = Toplevel(root)
    signup.title("Sign up page")

    global temp_name
    global temp_user
    global temp_password
    global temp_email
    global temp_phone
    global notif

    temp_name = StringVar()
    temp_user = StringVar()
    temp_password = StringVar()
    temp_email = StringVar()
    temp_phone = StringVar()

    Label(signup, text="Please Enter Your Details :) ", bg="purple", fg="white", pady=10,
          font="Times 15 bold italic").grid()
    Label(signup, text="Name", pady=5, padx=5, font="Times 10 bold italic").grid(row=1, column=0, sticky=W)
    Entry(signup, textvariable=temp_name).grid(row=1, column=1)
    Label(signup, text="Username", pady=5, padx=5, font="Times 10 bold italic").grid(row=2, column=0, sticky=W)
    Entry(signup, textvariable=temp_user).grid(row=2, column=1)
    Label(signup, text="Password", pady=5, padx=5, font="Times 10 bold italic").grid(row=3, column=0, sticky=W)
    Entry(signup, textvariable=temp_password, show='*').grid(row=3, column=1)
    Label(signup, text="Email", pady=5, padx=5, font="Times 10 bold italic").grid(row=4, column=0, sticky=W)
    Entry(signup, textvariable=temp_email).grid(row=4, column=1)
    Label(signup, text="Phone", pady=5, padx=5, font="Times 10 bold italic").grid(row=5, column=0, sticky=W)
    Entry(signup, textvariable=temp_phone).grid(row=5, column=1)

    notif= Label(signup, font="calibri 9 italic" )
    notif.grid(row=6,sticky=N,pady=10)

    Button(signup, text="signup", bg="pink", fg="yellow", pady=5, padx=5, font="Times 10 bold italic", borderwidth=4
           , command=finish).grid(row=7, sticky="n")


root =Tk()
root.geometry ("400x400")
root.minsize(200,100)
root.title("Banking app")

# images is inserted
image=Image.open("bankimg.jpg")
image=image.resize((150,150))
pic= ImageTk.PhotoImage(image)
Label(root,image=pic).grid(row=0 , column=1)

global log_notif
log_notif= Label(root, font="calibri 9 italic" )
log_notif.grid(row=6 , column=1)

# setting up username
username=Label(text="Username" , bg="orange", padx=20, pady=20,relief=GROOVE, borderwidth=5, fg="white" , font="Times 15 bold italic")
username.grid(row=1, column=0)
global log_name
log_name=StringVar()
e1=Entry(root,textvariable=log_name).grid(row=1, column=1)

# setting up password
password=Label(text="Password" , bg="blue", padx=20, pady=20,relief=GROOVE, borderwidth=5, fg="white" , font="Times 15 bold italic")
password.grid(row=2, column=0)
global magicword
magicword=StringVar()
e2=Entry(root,textvariable=magicword,show="*").grid(row=2, column=1)

# setting up buttons
Button(text="submit", bg="red", fg="white", font="Times 12 bold " , relief=RIDGE ,command=login).grid(row=4,column=0,padx=20, pady=10)
Button(text="SignUp", bg="black", fg="white", font="Times 12 bold " , relief=RIDGE,command=SIGNUP ).grid(row=4, column=3,padx=20, pady=10)




root.mainloop()
