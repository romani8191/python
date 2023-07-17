def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print('the no is composit')
            break

    else:
        print("it's a prime no")

n=int(input("enter any no.: "))

print(prime(n))