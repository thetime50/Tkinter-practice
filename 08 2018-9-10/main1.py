#-*- conding: utf-8 -*-
import queue
import threading
import time

plock = threading.Lock()
def secure_print(*args, sep=' ', end='\n', file=None):
	global plock
	plock.acquire()
	eval('print('+str(args)[1:-1]+',sep=sep,end=end,file=file)')
#	print(eval(str(args)[1:-1]),sep=sep,end=end,file=file)
	plock.release()

class queue_thread(threading.Thread):
	def __init__(self,name,q):
		threading.Thread.__init__(self)
		self.name=name
		self.q=q
	def run(self):
		secure_print('start thread:',self.name)
		while not self.q.empty():
			data=self.q.get()
			secure_print(self.name,':',data)
			time.sleep(1)
		secure_print('end thread:',self.name)

thread_name=['t1','t2','t3']
thread_list=[]
qdata=['a','b','c','d','e','f','g','h']
qu=queue.Queue()
for i in qdata:
	qu.put(i)
for i in thread_name:
	t=queue_thread(i,qu)
	thread_list.append(t)
	t.start()

for i in thread_list:
	i.join()
print('all end')
