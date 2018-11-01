#-*- coding: utf-8 -*-
import tkinter
import time
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
	def __init__(self,x,a,v=0,vmax=0):
		self._x=x
		self._a=a
		self._tim=time.time()
		self._v=v
		self._vmax=vmax
	def start_move_delta(self,delta_x):
		self._tim = time.time()
		self._delta_x=delta_x

		current_vmax=(2*self._a*self._delta_x)**0.5
		if(current_vmax<self._vmax):
			self._current_vmax=current_vmax
		else:
			self._current_vmax=self._vmax

		self._slow_down_s=0.5*self._current_vmax**2/self._a

	def start_move_delta(self, des_x):
		self._start_move_delta(self._des_x-self._x)

	def move_cb(self):
		now_tim=time.time()*1000
		delta_tim=now_tim-self._tim
		if(self._delta_x<self._slow_down_s):
			self._v-=delta_tim*self._a


def tk_add_canvas(rot,wind):
	ret=tkinter.Canvas(rot,bg='white',width=wind.w,height=wind.h)
	ret.place(x=wind.x,y=wind.y)#,anchor=tkinter.CENTER)
	return ret
root=tkinter.Tk()
root.minsize(Wind_w,Wind_h)
root.resizable(False,False)

cv0=tk_add_canvas(root,cv0_w)
cv1=tk_add_canvas(root,cv1_w)
print(9**0.5)




root.mainloop()
