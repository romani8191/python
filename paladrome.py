for a in range(1,1001):
    rev_a=0

    while(a!=0):
        b=a%10
        rev_a=rev_a*10 + b
        a //= 10

        str(rev_a)

    for str(a)==str(rev_a):
        print(a,rev_a)
        print(f"the {a} is prime")