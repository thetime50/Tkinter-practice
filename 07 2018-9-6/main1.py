#-*- coding: utf-8 -*-
import threading
import time
import math

def put_list(li,n=3):
	tablen=4
	cnt=0
	lens=[len(str(i)) for i in li]
	maxlen=max(lens)
	wide=math.ceil((maxlen+2+1)/tablen)
	print('[')
	for i in li:
		print('\''+str(i)+'\'',end='')
		print('	'*(wide-(len(i)+2)//tablen),end='')
		cnt+=1
		if cnt%n==0:
			print('')
	print(']')
#
put_list(dir(threading))
put_list(dir(threading.Thread))
#################################################
exitFlag=0
class TeatThread(threading.Thread):
	def __init__(self,trID,name,count):
		threading.Thread.__init__(self)
		self.trID=trID
		self.name=name
		self.count=count
	def run(self):#会自动选择run这个成员函数
		print(self.name,'run() start')
		print_time(self.name,self.count,2)
		print(self.name,'run() end')

def print_time(trName,count,delay):
	global exitFlag
	while count:
		if exitFlag:
			threading,exit()
		time.sleep(delay)
		print(trName,str(time.ctime(time.time())),count,exitFlag)
		count-=1
	exitFlag=True

#
tr1=TeatThread(1,'tr1',2)
tr2=TeatThread(2,'tr2',4)

tr1.start()
time.sleep(0.1)
tr2.start()
tr1.join()
tr2.join()
print('all end')