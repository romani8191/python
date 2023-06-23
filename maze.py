from tkinter import *
import tkinter.messagebox as tmsg
import mysql.connector


# ---------------------------------Signup page-------------------------------------------------------------------------


def finish():
    tmsg.showinfo("Welcome","You'r registeration has been done :)")

def SIGNUP():
    signup=Toplevel(root)
    signup.title("Sign up page")

    temp_name = StringVar()
    temp_user=StringVar()
    temp_password=StringVar()
    temp_email=StringVar()
    temp_phone=StringVar()



    Label(signup, text="Please Enter Your Details :) ", bg="purple", fg="white", pady=10, font="Times 15 bold italic").grid()
    Label(signup, text="Name" , pady=5, padx=5, font="Times 10 bold italic" ).grid(row=1, column=0, sticky=W )
    Entry(signup, textvariable=temp_name).grid(row=1, column=1)
    Label(signup, text="Username" , pady=5, padx=5, font="Times 10 bold italic" ).grid(row=2, column=0, sticky=W)
    Entry(signup, textvariable=temp_user).grid(row=2, column=1)
    Label(signup, text="Password" , pady=5, padx=5, font="Times 10 bold italic" ).grid(row=3, column=0, sticky=W)
    Entry(signup, textvariable=temp_password).grid(row=3, column=1)
    Label(signup, text="Email" , pady=5, padx=5, font="Times 10 bold italic" ).grid(row=4, column=0, sticky=W)
    Entry(signup, textvariable=temp_email).grid(row=4, column=1)
    Label(signup, text="Phone" , pady=5, padx=5, font="Times 10 bold italic" ).grid(row=5, column=0, sticky=W)
    Entry(signup, textvariable=temp_phone).grid(row=5, column=1)

    Button(signup, text="signup", bg="pink", fg="yellow",pady=5, padx=5, font="Times 10 bold italic" ,borderwidth=4
           ,command=finish).grid(row=6,sticky="n")

    ename=name.get()
    euser=name.get()
    epassword=magicword.get()
    eemail=temp_email.get()
    ephone=temp_phone.get()



    db = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="starGirl"
        )
    i = db.cursor()
    i.execute("insert into db values('" +temp_user+ "', '" + temp_password + "', '" + temp_name + "', '" + temp_email + "', '" + temp_phone + "')")
    i.execute("commit")

    tmsg.showinfo("Welcome", f"Welcome {temp_name} :) ")
    db.close()

# -----------------------------------master page-----------------------------------------------
def insert():
    ename=name.get()
    emagic=magicword.get()

    if (ename=="" or emagic=="" ):
        tmsg.showinfo("error","Please enter the data :( ")
    else:
        db = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="starGirl"
        )
        for name_check in name:
            if name_check == name:
                tmsg.showinfo("error", " Account exists ")
            else:
                i=db.cursor()
                i.execute("insert into db values('"+ename+"', '"+emagic+"')")
                i.execute("commit")

                tmsg.showinfo("Welcome", f"Welcome {ename} :) ")
        db.close()
        SUBMIT()



def SUBMIT():
    mpage=Toplevel(root)
    mpage.geometry("400x230")
    mpage.title("Bank of Hindustaan")
    mymenue = Menu(mpage)
    mymenue.add_command(label="New Account", command=OpAcc)
    mymenue.add_command(label="List Account", command=ListAcc)
    mymenue.add_command(label="Search", command=search)
    mymenue.add_command(label="Deposit", command=depo)
    mymenue.add_command(label="Withdraw", command=withdraw)
    mymenue.add_command(label="Exit", command=quit)

    mpage.config(menu=mymenue)



bank=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="starGirl"
)

print("database created")
mycursor= bank.cursor()

mycursor.execute('drop table if exists bank')
print('bank table dropped')


mycursor.execute('create table bank(AccountNo int primary key, name varchar(25),balance int(50))')
print ('table created')

sql = 'insert into bank (AccountNo ,name, balance) values(%s,%s,%s)'
val=[
    (1001,"Romani",300000),
    (1002,"Prerna",200000),
    (1003,"Nitesh",100000)
]

mycursor.executemany(sql,val)
bank.commit()
print(mycursor.rowcount,"Record was inserted")

mycursor.execute("select * from bank")
result=mycursor.fetchall()
for records in result:
    print(records)


# def info(self):
#     name = input('Enter your name: ')
#     print(name)
#     AccountNo = int(input('Enter your account no.: '))
#     print(AccountNo)
#     pin = int(input('Enter the pin: '))
#     print(pin)
#
def OpAcc():
    n=input("Please enter your name : ")
    acc=int(input("enter the account no. : "))
    bal=int(input("Enter the balance"))
    data=(acc,n,bal)
    sql="insert into bank values(%s, %s, %s)"
    mycursor=bank.cursor()
    mycursor.execute(sql,data)
    bank.commit()
    print("Your Account has been created :)")
    SUBMIT()
#
def depo():
    amount=int(input("Enter the amount u want to deposit : "))
    acc=int(input("Enter the account no. : "))
    a="select balance from bank where AccountNo=%s"
    data=(acc,)
    mycursor = bank.cursor()
    mycursor.execute(a, data)
    result=mycursor.fetchone()
    total=result[0]+amount
    sql="update bank set balance=%s where AccountNo=%s"
    d=(total,acc)
    mycursor.execute(sql,d)
    bank.commit()
    SUBMIT()
#
def withdraw():
    amount=int(input("Enter the amount u want to deposit : "))
    acc=int(input("Enter the account no. : "))
    a="select balance from bank where AccountNo=%s"
    data=(acc,)
    mycursor = bank.cursor()
    mycursor.execute(a, data)
    result=mycursor.fetchone()
    total=result[0]-amount
    sql="update bank set balance=%s where AccountNo=%s"
    d=(total,acc)
    mycursor.execute(sql,d)
    bank.commit()
    SUBMIT()


def search():
    ac=input("Please enter the account no : ")
    a="select * from bank where AccountNo=%s"
    data=(ac,)
    c=bank.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print(f"The info of the required account is : {myresult}")
    SUBMIT()
#
def ListAcc():
    mycursor.execute("select * from bank")
    result = mycursor.fetchall()
    for records in result:
        print(records)
    SUBMIT()
#
#
#
# def main():
#     print("""
#     1 New Account
#     2 List Account
#     3 Search Account
#     4 Deposit
#     5 Withdraw
#     6 Exit
#     """)
#     choice=input("Please enter your choice : ")
#     if choice=="1":
#         OpAcc()
#     elif choice=="2":
#         ListAcc()
#     elif choice=="3":
#         search()
#     elif choice=="4":
#         depo()
#     elif choice=="5":
#         withdraw()
#     else:
#         print("Thanks for visiting :) ")
#
# main()


root =Tk()
root.geometry ("400x230")
root.minsize(200,100)

# setting up username
username=Label(text="Username" , bg="orange", padx=20, pady=20,relief=GROOVE, borderwidth=5, fg="white" , font="Times 15 bold italic")
username.pack(side=TOP , anchor="nw", fill=X)

name=StringVar()
Entry(root,textvariable=name).pack(fill=X)

# setting up password
password=Label(text="Password" , bg="blue", padx=20, pady=20,relief=GROOVE, borderwidth=5, fg="white" , font="Times 15 bold italic")
password.pack(side=TOP , anchor="nw", fill=X)

magicword=StringVar()
Entry(root,textvariable=magicword).pack(fill=X)

# setting up buttons
Button(text="submit", bg="red", fg="white", font="Times 12 bold " , relief=RIDGE ,command=insert).pack(side="left", anchor="sw",padx=20, pady=10)
Button(text="SignUp", bg="black", fg="white", font="Times 12 bold " , relief=RIDGE , command=SIGNUP).pack(side="right", anchor="se",padx=20, pady=10)




root.mainloop()
