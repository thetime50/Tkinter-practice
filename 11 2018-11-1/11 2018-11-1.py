#-*- coding: utf-8 -*-
import tkinter
import time
import math

class WindClass:
	def __init__(self,x,y,w,h):
		self.x=x
		self.y=y
		self.w=w
		self.h=h

Win_interval=4
cv0_w=WindClass(Win_interval,Win_interval,600,20)
cv1_w=WindClass(Win_interval,2*Win_interval+cv0_w.h,600,500)

Wind_w=610
Wind_h=550


class OneDimensionalMoveClass:
	def __init__(self, x, a, v0=0, vmax=0):
		self._x0 = x
		self._v0 = v0
		self._x = x
		self._a = a
		self._vmax = vmax
		self._current_vmax = vmax
		self._tim0 = time.time()
		self._t1 = 0
		self._t2 = 0
		self._t3 = 0
		self._des_x = x
		self._current_a = a
		self._s0=0
		self._s1=0

	def get_v(self,tim=0):
		if tim==0:
			tim=time.time()
		if(abs(self._x-self._des_x)<0.000001):
			return 0
		if tim>self._tim0+self._t2:
			t=tim-self._tim0-self._t2
			v= self._v0+self._current_a*t
		elif tim > self._tim0 + self._t1:
			v=self._current_vmax
		else:
			t = tim - self._tim0
			v=self._current_vmax-self._current_a*t
		return v
	def start_move_des(self, des_x):
		tim=time.time()
		v=self.get_v(tim)
		self._tim0 = tim
		self._x0 = self._x
		self._v0 = v

		self._des_x = des_x
		delta_x = des_x - self._x
		self._current_a = math.copysign(self._a, delta_x)

		current_vmax = (self._current_a * (delta_x) + 0.5 * v ** 2) ** 0.5
		if current_vmax < self._vmax or self._vmax==0:
			current_vmax = math.copysign(current_vmax, delta_x)
			self._t2=self._t1=(current_vmax-self._v0)/self._current_a
		else:
			current_vmax = math.copysign(self._vmax, delta_x)
			self._t1=(current_vmax-self._v0)/self._current_a
			self._t2=self._t1+(delta_x - (current_vmax**2-self._v0**2)/2/self._current_a - current_vmax**2/self._current_a/2)/current_vmax
		self._current_vmax=current_vmax

		if abs(v - current_vmax) > 0.0001 and \
				math.copysign(1, v) == math.copysign(1, current_vmax) and \
				abs(v) > abs(current_vmax):
			# 不接近 同号 当前速度更大
			self._v0=self._v = current_vmax
			self._t1=self._t2=0

		self._s0=(self._current_vmax**2-self._v0**2)/2/self._current_a
		self._s1=(self._t2-self._t1)*self._current_vmax
		self._t3=self._t2+(delta_x-self._s0-self._s1)/current_vmax*2

	def start_move_delta(self, delta_x):
		self._start_move_delta(self._x + delta_x)

	def move_cb(self):
		tim=time.time()
		old_x=self._x
		if(tim>= self._tim0+self._t3):
			self._x=self._des_x
			return old_x,self._x
		elif tim>self._tim0+self._t2:
			t=tim-self._tim0-self._t2
			delta_x=self._s0 + self._s1 + self._current_vmax*t-0.5*self._current_a*t**2
			self._x=self._x0+delta_x
		elif tim > self._tim0 + self._t1:
			t=tim-self._tim0-self._t1
			delta_x=self._s0 + t*self._current_vmax
			self._x=self._x0+delta_x
		else:
			t = tim - self._tim0
			delta_x=self._v0*t+0.5*self._current_a*t**2
			self._x=self._x0+delta_x
		return old_x,self._x


'''
class OneDimensionalMoveClass:
	def __init__(self,x,a,v=0,vmax=0):
		self._x0		= x
		self._x			= x
		self._a			= a
		self._tim0		= time.time()
		self._t1		=0
		self._t2		=0
		self._v			= v
		self._des_x		= x
		self._current_a = a

	def start_move_des(self, des_x):
		self._tim = time.time()
		self._des_x = des_x
		delta_x = des_x-self.x
		self._current_a = math.copysign(self._a, delta_x)

		current_vmax = (self._current_a * (delta_x) + 0.5 * self._v ** 2) ** 0.5
		if current_vmax < self._vmax:
			self._current_vmax = math.copysign(current_vmax, delta_x)
		else:
			self._current_vmax = math.copysign(self._vmax, delta_x)

		if abs(self._v-self._current_vmax) > 0.0001 and\
				math.copysign(1,self._v)==math.copysign(1,self._current_vmax)  and\
				abs(self._v) > abs(self._current_vmax):
			#不接近 同号 当前速度更大
			self._v = self._current_vmax
		self._slow_down_s = 0.5*self._current_vmax**2/self._current_a

	def start_move_delta(self, delta_x):
		self._start_move_delta(self._x+delta_x)

	def move_cb(self):
'''

def tk_add_canvas(rot,wind):
	ret=tkinter.Canvas(rot,bg='white',width=wind.w,height=wind.h)
	ret.place(x=wind.x,y=wind.y)#,anchor=tkinter.CENTER)
	return ret
root=tkinter.Tk()
root.minsize(Wind_w,Wind_h)
root.resizable(False,False)

cv0=tk_add_canvas(root,cv0_w)
cv1=tk_add_canvas(root,cv1_w)

od_move=OneDimensionalMoveClass(10,1000)
def draw_cv0_recttangle(cv,x,y,w,h,fill='black',width=0):
	#print(x,y,w,h,fill,width)
	if w>1:	w-=1
	else: w=0
	if h>1: h-=1
	else: h=0
	return cv.create_rectangle(x-w/2, y-h/2, x+w/2, y+h/2, fill=fill, width=width)
def change_recttangle(cv,rect,x,y,w,h):
	#print(x,y,w,h,fill,width)
	if w>1:	w-=1
	else: w=0
	if h>1: h-=1
	else: h=0
	return cv.coords(rect,x-w/2, y-h/2, x+w/2, y+h/2)

rect0=draw_cv0_recttangle(cv0,10,cv0_w.h/2,cv0_w.h*0.01,cv0_w.h*0.6,"black")
print(type(rect0),"  ",rect0)
def cv0_b1_fun(event):
	#print(event)
	od_move.start_move_des(event.x)
	#draw_cv0_recttangle(cv0,event.x, cv0_w.h / 2, 2, cv0_w.h * 0.6, fill="red")

def cv0_after_fun():
	old_x,x=od_move.move_cb()
	if old_x!=x:
		#draw_cv0_recttangle(cv0,old_x, cv0_w.h / 2, cv0_w.h*0.01, cv0_w.h * 0.6, fill="white")
		#draw_cv0_recttangle(cv0,x, cv0_w.h / 2, cv0_w.h*0.01, cv0_w.h * 0.6, fill="black")
		change_recttangle(cv0,rect0,x, cv0_w.h / 2, cv0_w.h*0.01, cv0_w.h * 0.6)
		#print(x)
	cv0.after(20, cv0_after_fun)
cv0.bind('<B1-Motion>',cv0_b1_fun)
cv0.bind('<Button-1>',cv0_b1_fun)
cv0.after(20, cv0_after_fun)


root.mainloop()