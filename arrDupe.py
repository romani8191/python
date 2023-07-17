a=[1,2,2,4,5,6,7,8,9,10,10,5]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if (a[i]==a[j]):
            print(a[i])