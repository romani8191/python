a = input("enter the student details: ")

sub1= int(input("enter the student's marks in subject1: "))
sub2 = int(input("enter the student's marks in subject2: "))
sub3= int(input("enter the student's marks in subject3: "))
sub4 = int(input("enter the student's marks in subject4: "))


print (a)
print(sub1)

avg=int((sub1+sub1+sub1+sub1)/4)
print (avg)

if(avg>80):
    print("your grade is O")
elif(avg>60 & avg<=80):
    print("your grade is A")
elif(avg>50 & avg<=60):
    print("your grade is B")
else:
    print("Work a bit harder :)")