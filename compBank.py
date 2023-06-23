import mysql.connector

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


def info(self):
    name = input('Enter your name: ')
    print(name)
    AccountNo = int(input('Enter your account no.: '))
    print(AccountNo)
    pin = int(input('Enter the pin: '))
    print(pin)

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
    main()

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
    main()

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
    main()


def search():
    ac=input("Please enter the account no : ")
    a="select * from bank where AccountNo=%s"
    data=(ac,)
    c=bank.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print(f"The info of the required account is : {myresult}")
    main()

def ListAcc():
    mycursor.execute("select * from bank")
    result = mycursor.fetchall()
    for records in result:
        print(records)
    main()



def main():
    print("""
    1 New Account
    2 List Account
    3 Search Account
    4 Deposit
    5 Withdraw
    6 Exit
    """)
    choice=input("Please enter your choice : ")
    if choice=="1":
        OpAcc()
    elif choice=="2":
        ListAcc()
    elif choice=="3":
        search()
    elif choice=="4":
        depo()
    elif choice=="5":
        withdraw()
    else:
        print("Thanks for visiting :) ")

main()



