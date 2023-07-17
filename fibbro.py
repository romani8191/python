def fabbro(n):
    n1=0
    n2=1
    sum=0
    for i in range(n):
        print(sum,end=' ')
        n1=n2
        n2=sum
        sum=n1+n2
    return(sum)
n=int(input("enter any number"))

fabbro(n)