a=int(input("enter a no A: "))
b=int(input("enter a no B: "))

print("Before swapping")
print(f"the value of A is: {a} and the value of b is {b} ")
 
a=int(((a+b)-(a-b))/2)
b=int(((a+b)+(a-b))/2)


print("After swapping")
print(f"the value of A is: {a} and the value of b is {b} ")
