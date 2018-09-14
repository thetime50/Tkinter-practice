#-*- coding: utf-8 -*-
import tkinter
import threading
import time

#acquire release
class secure_value:
	def __init__(self,value):
		self.value=value
		self.lock=threading.Lock()
	def set(self,value):
		self.lock.acquire()
		self.value=value
		self.lock.release()
	def get(self):
		self.lock.acquire()
		v=self.value
		self.lock.release()
		return v
	def pp(self,sleep_sec=0):
		self.lock.acquire()
		self.value=self.value+1
		if sleep_sec:
			time.sleep(sleep_sec)
		self.lock.release()
sv=secure_value(0)

class settime_thread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		global sv
		if False:
			while True:
				sv.pp()
				time.sleep(1)
		else:
			while True:
				sv.pp(3)#另一个线程里不一定会抢到

class puttime_thread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		global sv
		while True:
			time.sleep(1)
			v=sv.get()
			print(v)

st=settime_thread()
pt=puttime_thread()
st.start()
pt.start()
st.join()
pt.join()
print('end')