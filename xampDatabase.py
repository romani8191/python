import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password='',
    database='starGirl'
)
print('Database created')

mycursor=mydb.cursor()

mycursor.execute('drop table if exists celib')
print('celib table dropped')

mycursor.execute('create table celib(id int auto_increment primary key, name varchar(25),albums varchar(50), age varchar(5), listners varchar(10))')
print ('table created')

sql = 'insert into celib (name, albums, age, listners) values(%s,%s,%s,%s)'
val=[
    ('Taylor', 'ME',30,'11mill'),
    ('Ed Sheen ', 'equation', 27, '10mill'),
    ('Justin', 'friends', 26, '20mill'),
    ('BTS', 'love yourself', 30, '1bill')

]

mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"Record was inserted")

print()

mycursor.execute("select * from celib")
result=mycursor.fetchall()
for records in result:
    print(records)

mycursor.execute('select * from celib where age>27')
a=mycursor.fetchall()
for r in a:
    print(a)

mycursor.execute('update celib set age=33 where id=4')
mydb.commit()
print(mycursor.rowcount,'records changed')
z=mycursor.fetchall()
for x in z:
    print(x)