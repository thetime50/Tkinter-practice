#-*- conding: utf-8 -*-

import tkinter
import PIL.Image,PIL.ImageTk
import math
import time

root=tkinter.Tk()
cv=tkinter.Canvas(root,width=600,heigh=400,bg='white')
#cv.place(x=0,y=0)
'''
tkimg=lambda w,h:PIL.ImageTk.PhotoImage(img.resize((w,h),PIL.Image.ANTIALIAS))
bimage=tkimg(10,10)
cv.create_image(200,200,image=bimage,anchor=tkinter.CENTER)
aimage=tkimg(100,100)
cv.create_image(200,200,image=aimage,anchor=tkinter.SE)#是参考点相对于图片的方位
'''
class DrawImageClass:
	img = PIL.Image.open('./img/timg.png')
	tkimg = lambda self, w, h: PIL.ImageTk.PhotoImage(self.img.resize((w, h), PIL.Image.ANTIALIAS))

	def __init__(self):
		self.puten=False
		self.motion_cnt=0
		self.press_cnt = 0
		self.release_cnt = 0
		self.w=20
		self.h=20
		self.image =[]
		self.checked=False
		self.ctrl = False
	def draw(self):
		if self.ctrl:
			w=h=min(self.w,self.h)
		else:
			w=self.w
			h=self.h
		self.image[-1]=self.tkimg(w, h)
		cv.create_image(self.x, self.y, image=self.image[-1], anchor=tkinter.CENTER)
	def B1Press_fun(self,event):
		self.press_cnt+=1
		if self.puten: print('bpress',str(event),self.press_cnt)

		self.checked =True
		self.resize=False
		self.x=event.x
		self.y=event.y
		self.image.append(self.tkimg(self.w, self.h))
		cv.create_image(self.x, self.y, image=self.image[-1], anchor=tkinter.CENTER)

	def B1Motion_fun(self,event):
		self.motion_cnt+=1
		if self.puten: print('bmotion',str(event),self.motion_cnt)

		if abs(event.x - self.x) * 2 > self.w or self.resize:
			self.resize = True
			self.w = math.ceil(abs(event.x - self.x)*2)
			if self.w < 1: self.w = 1
		if abs(event.y - self.y) * 2 > self.h or self.resize:
			self.resize = True
			self.h = math.ceil(abs(event.y - self.y)*2)
			if self.h<1:self.h=1
		self.draw()
		# print(self.x, self.y,event.x, event.y,self.w, self.h)

	def B1Release_fun(self,event):
		self.release_cnt+=1
		if self.puten: print('brelease',str(event),self.release_cnt)

		self.checked =False
		#del self.image[-1]
	def CPress_fun(self,event):
		del self.image
		self.image = []
	def CtlPress_fun(self,event):
		self.ctrl = True
		if self.checked:
			self.draw()
	def CtlRelease_fun(self,event):
		self.ctrl=False
		if self.checked:
			self.draw()

	def __del__(self):
		print('__del__')

DrawImage=DrawImageClass()

cv.bind('<B1-Motion>',DrawImage.B1Motion_fun)
cv.bind('<Button-1>',DrawImage.B1Press_fun)
cv.bind('<ButtonRelease-1>',DrawImage.B1Release_fun)
root.bind('<c>',DrawImage.CPress_fun)
root.bind('<Control_L>',DrawImage.CtlPress_fun)
root.bind('<KeyRelease-Control_L>',DrawImage.CtlRelease_fun)

cv.pack()
root.mainloop()
