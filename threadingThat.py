import threading
import time

def fun(seconds):
	print(f'Sleeping for {seconds} seconds')
	time.sleep(seconds)





time1=time.perf_counter()
# fun(4)
# fun(2)
# fun(1)


t1=threading.Thread(target=fun , args=[4])
t2=threading.Thread(target=fun , args=[2])
t3=threading.Thread(target=fun , args=[1])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()



time2=time.perf_counter()
print(time2-time1)




