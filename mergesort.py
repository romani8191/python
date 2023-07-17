a=[9,7,5,3,1]
b=[8,6,4,2,0]
a.sort()
b.sort()
c=a+b
print(c)

c.sort()
print(c)

def combine(a,b):
    new=[]
    for i in range(len(a)):
        new.append(b[i])

        new.append(a[i])
    return new
print(combine(a,b))