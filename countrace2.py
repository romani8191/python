import queue
import threading, time, random

def fun(i):
    count=0
    while count <= i  :
        count=count+1
        print(count)

a=threading.Thread(target=fun , args=[99,])

b=threading.Thread(target=fun, args=[99,] )

c=threading.Thread(target=fun, args=[99,] )


a.start()
b.start()
c.start()

def func(id, result_queue):
    print("Thread", id)
    result_queue.put((id, 'done'))

def main():
    q = queue.Queue()
    threads = [ threading.Thread(target=func, args=(i, q)) for i in range(3) ]
    for th in threads:
        th.daemon = True
        th.start()

    result1 = q.get()
    result2 = q.get()

    print("Second result: {}".format(result2))

if __name__=='__main__':
    main()