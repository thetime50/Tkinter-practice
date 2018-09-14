#-*- coding: utf-8 -*-
import _thread
import time
import sys

def put_strarr(s):
	for i in s:
		print('\''+str(i)+'\'')
## 线程 ##
def print_time(thread_name,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count+=1
		print('%s: %s %d'%(thread_name,time.ctime(time.time()),count))
	print(thread_name,'end')
#	exit()
#
try:
	_thread.start_new_thread(print_time,('Thread 1',1))
	tr2=_thread.start_new_thread(print_time,('Thread 2',3))
except:
	put_strarr(sys.exc_info())
	print('Error')
while True:
	pass