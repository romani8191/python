import threading

def mult(i):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')

a=threading.Thread(target=mult, args=[2])
b=threading.Thread(target=mult, args=[3])
c=threading.Thread(target=mult, args=[5])

a.start()
a.join()

b.start()
b.join()

c.start()
c.join()




