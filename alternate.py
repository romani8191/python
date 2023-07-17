a=[1,3,5,7]
b=[2,4,6,8]
c=a[0::2]
d=b[0::2]
e=c+d
print(e)


def combine(a,b):
    new=[]
    for i in range(len(a)):
        new.append(a[i])
        new.append(b[i])
    return new
print(combine(a,b))