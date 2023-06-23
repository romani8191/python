import threading
count=0
flag=False

def fun(i):
    global count
    while count <= i  :
        count=count+1
        print(count)
        if count==100:
            flag=True
            break
    if flag:
        if a==100:
            print(f'the thread got over is winner a \n')

        elif b==100:
            print(f'the thread got over is winner b \n')
        else:
            print(f'the thread got over is winner c \n')
    else :
        print('processing')





a=threading.Thread(target=fun , args=[99,])

b=threading.Thread(target=fun, args=[99,] )

c=threading.Thread(target=fun, args=[99,] )


a.start()
b.start()
c.start()








