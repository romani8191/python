def factorial(b):
    factorial=1
    for i in range(b):
        factorial*=i+1
    return factorial
print(factorial(5))

for i in range(6):
    print(factorial(i))
