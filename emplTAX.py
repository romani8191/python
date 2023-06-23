import mysql.connector
import numpy

emp=mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='starGirl'
)
print('database created')

mycursor=emp.cursor()

mycursor.execute("drop table if exists employee")
print("The table has been deleted")

mycursor.execute("create table employee(id int auto_increment primary key, name varchar(30),department varchar(50), salary int(50))")
print("table employee has been created :)")

sql="insert into employee (name, department, salary) values(%s,%s,%s)"
val=[
    ("Mani", "AI", 100000),
    ("Parul", "JAVA", 90000),
    ("Prerna", "WebD", 120000),
    ("Puneet", "DSA", 150000),
    ("Keshav", "webD", 70000),
    ("Nitesh", "webD", 100000)
]
mycursor.executemany(sql,val)
emp.commit()
print(mycursor.rowcount,"Record was inserted")

print()

mycursor.execute("select * from employee where salary>=100000")
a=mycursor.fetchall()
for rec in a:
    print(rec)

print()

mycursor.execute("select * from employee order by employee.salary desc limit 2,2")
third=mycursor.fetchall()
print(f"the person having 3 rd highest salary is {third}")

mycursor.execute("Alter table employee ADD tax int(10)")
print("a new column has been added :)")

mycursor.execute("select id ,salary from employee ")
i=mycursor.fetchall()
print (i)


i=100000

if i <= 70000:
    tax = ((1.6 * i) / 100)
elif i <= 120000:
    tax = ((1.8 * i) / 100)
else:
    tax = ((2.6 * i) / 100)
print(tax)

tax1=int((1.8*100000)/100)
t1=print(tax1)
mycursor.execute('update employee set tax=1800 where id =1')
emp.commit()


tax2=int((1.6*90000)/100)
t2=print(tax2)
mycursor.execute('update employee set tax=1440 where id =2')
emp.commit()

tax3=int((1.8*120000)/100)
t3=print(tax3)
mycursor.execute('update employee set tax=2160 where id =3')
emp.commit()

tax4=int((2.6*150000)/100)
t4=print(tax4)
mycursor.execute('update employee set tax=3900 where id =4')
emp.commit()

tax5=int((1.6*70000)/100)
t5=print(tax5)
mycursor.execute('update employee set tax=1120 where id =5')
emp.commit()

tax6=int((1.8*100000)/100)
t6=print(tax6)
mycursor.execute('update employee set tax=1800 where id =6')
emp.commit()


# sql1 = 'insert into employee (tax) values(%s)'
# val1=[
#     (1800),
#     (1440),
#     (2160),
#     (3900),
#     (1120),
#     (1800)
#
# ]
# mycursor.executemany(sql1,val1)
# emp.commit()
# print("Record was inserted")
#
# print()
