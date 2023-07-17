a=int(input("Enter a 3 digit no.: "))
print (a)
rev_a=0

while(a!=0):
    b=a%10
    rev_a=rev_a*10 + b
    a //= 10

print ("Reversed no is : " + str(rev_a))


