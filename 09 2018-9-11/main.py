#-*- coding： utf-8 -*-

import tkinter
import io
from PIL import Image,ImageTk
import threading
import time


Unit_x_cnt=40
Unit_y_cnt=50
Unit_l=10
Canvas_wide=Unit_x_cnt*Unit_l
Canvas_hight=Unit_y_cnt*Unit_l
Option_region_wide=400
Win_interval=4
Win_wide=Win_interval+Canvas_wide+Win_interval+Option_region_wide+Win_interval
Win_high=Win_interval+Canvas_hight+Win_interval

root=tkinter.Tk()
root.minsize(Win_wide,Win_high+6)
root.resizable(0,0)
cv=tkinter.Canvas(root,bg='white',width=Canvas_wide,height=Canvas_hight)
cv.place(x=Win_interval,y=Win_interval)
#root.winfo_width()
#root.winfo_height()
print(dir())
class draw_unit_c:
	''''''
	img_list=['empty','food',\
		'head',\
		'tail',\
		'body_NE', 'body_SE', 'body_SW', 'body_NW', 'body_NS', 'body_WE']
	unit_img={x:Image.open('./img/'+x+'.png').resize((Unit_l,Unit_l),Image.ANTIALIAS) 	for x in img_list}

	def draw(self,x,y,dire):
		global cv,Unit_l
		#cv.create_image(x*Unit_l,y*Unit_l,image=self.unit_img[sr])

def rectangle(x,y,w,h,colour):
	cv.create_rectangle(x,y,x+w,y+h,fill=colour,width=1)
def draw_unit_pixel(ux,uy,ul,px,py):
	pixel_l=ul/6
	x = ux * ul+px*pixel_l
	y = uy * ul+py*pixel_l
	rectangle(x, y, pixel_l, pixel_l, 'black')
def draw_unit_pixels(ux,uy,ul,px1,py1,px2,py2):
	for px in range(px1,px2+1):
		for py in range(py1,py2+1):
			draw_unit_pixel(ux,uy,ul,px,py)

du=draw_unit_c()
def draw_unit(sunit,clean=False):
	#du.draw(x,y,dire)
	global cv, Unit_l
	xoffset = sunit.x * Unit_l
	yoffset = sunit.y * Unit_l
	rectangle(xoffset,yoffset,Unit_l,Unit_l,'blue')
	if clean:#clear
		pass
	elif sunit.prev!=None and sunit.next==None:#tail
		if sunit.dire=='N':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 2)
			draw_unit_pixel( sunit.x, sunit.y, Unit_l, 3, 3)
		if sunit.dire=='S':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 3, 3, 5)
			draw_unit_pixel( sunit.x, sunit.y, Unit_l, 3, 2)
		if sunit.dire=='W':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 2, 3)
			draw_unit_pixel( sunit.x, sunit.y, Unit_l, 3, 3)
		if sunit.dire=='E':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 3, 2, 5, 3)
			draw_unit_pixel( sunit.x, sunit.y, Unit_l, 2, 3)
	elif sunit.prev==None and sunit.next!=None:#head
		if sunit.dire=='N':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 1, 3, 1)
		if sunit.dire=='S':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 4)
		if sunit.dire=='W':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 1, 2, 1, 3)
		if sunit.dire=='E':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 4, 3)
		draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 2, 3, 3)
		if sunit.next.dire=='N':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 5)
		if sunit.next.dire=='S':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 1)
		if sunit.next.dire=='W':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 5, 3)
		if sunit.next.dire=='E':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 1, 3)
	elif sunit.prev!=None and sunit.next!=None:#body
		if sunit.dire=='N':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 1)
		if sunit.dire=='S':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 5)
		if sunit.dire=='W':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 1, 3)
		if sunit.dire=='E':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 5, 3)
		draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 2, 3, 3)
		if sunit.next.dire=='N':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 5)
		if sunit.next.dire=='S':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 1)
		if sunit.next.dire=='W':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 5, 3)
		if sunit.next.dire=='E':
			draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 1, 3)

class slither_unit_c:
	def __init__(self,x,y,dire,prev=None,next=None):
		self.prev=prev
		self.next=next
		self.dire=dire
		self.x=x
		self.y=y
	def __del__(self):
		if self.prev!=None:
			self.prev.next=self.next
		if self.next!=None:
			self.next.prev=self.prev

class slither_c:
	def __init__(self,x,y,n):
		self.head=None
		self.tail=None
		for i in range(n):
			self.append('E',x-i,y)
		p=self.head
		while p!=None:
			draw_unit(p)
			p=p.next
	def __del__(self):
		while self.head!=None:
			p=self.head
			self.head = self.head.next
			del p
	def append(self,dire,x,y):
		unit=slither_unit_c(x,y,dire,self.tail)
		if self.tail!=None:
			self.tail.next=unit
		if self.head==None:
			self.head = unit
		self.tail=unit
	def apphead(self,dire,x,y):
		unit=slither_unit_c(x,y,dire,None,self.head)
		if self.head!=None:
			self.head.prev=unit
		if self.tail==None:
			self.tail = unit
		self.head=unit
	def delend(self):
		if self.tail!=None:
			p=self.tail
			self.tail=self.tail.prev
			self.tail.next=None
			del p
	def move(self,food):
		y = self.head.y
		x = self.head.x
		if self.head.dire=='N':
			y-=1
		if self.head.dire=='S':
			y+=1
		if self.head.dire=='W':
			x-=1
		if self.head.dire=='E':
			x+=1
		if x>=Unit_x_cnt or x<0 or y>=Unit_y_cnt or y<0:
			return -1
		self.apphead(self.head.dire, x, y)
		draw_unit(self.head)
		draw_unit(self.head.next)
		if food==False:
			draw_unit(self.tail,True)
			self.delend()
			draw_unit(self.tail)
		return 0
	def change_head_dire(self,dire):
		if (self.head.prev.dire=='N'and dire!='S')and \
				(self.head.prev.dire == 'S' and dire != 'N') and \
				(self.head.prev.dire == 'W' and dire != 'E') and \
				(self.head.prev.dire == 'E' and dire != 'W'):
			self.head.dire=dire
			draw_unit(self.head)

if __name__=='__main__':
	root.mainloop()