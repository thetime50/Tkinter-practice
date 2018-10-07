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
Option_region_x_offset=Win_interval+Canvas_wide+Win_interval
Option_region_x_center=Option_region_x_offset+Option_region_wide/2
Win_wide=Option_region_x_offset+Option_region_wide+Win_interval
Win_high=Win_interval+Canvas_hight+Win_interval

root=tkinter.Tk()
root.minsize(Win_wide,Win_high+6)
root.resizable(0,0)
class room_c:
	def __init__(self,root):
		self.cv=tkinter.Canvas(root,bg='white',width=Canvas_wide,height=Canvas_hight)
		self.cv.place(x=Win_interval,y=Win_interval)
		self.unit_list=[['e' for y in range(Unit_y_cnt)] for x in range(Unit_x_cnt)]
		self.slither_cnt=0
		self.food_cnt=0
		self.unit_cnt=Unit_y_cnt*Unit_x_cnt
		#root.winfo_width()
		#root.winfo_height()
	class draw_unit_c:
		''''''
		img_list=['empty','food',\
			'head',\
			'tail',\
			'body_NE', 'body_SE', 'body_SW', 'body_NW', 'body_NS', 'body_WE']
		unit_img={x:Image.open('./img/'+x+'.png').resize((Unit_l,Unit_l),Image.ANTIALIAS) 	for x in img_list}

		def draw(self,x,y,dire):
			global Unit_l
			#cv.create_image(x*Unit_l,y*Unit_l,image=self.unit_img[sr])

	def rectangle(self,x,y,w,h,colour):
		self.cv.create_rectangle(x,y,x+w,y+h,fill=colour,width=1)
	def draw_unit_pixel(self,ux,uy,ul,px,py):
		pixel_l=ul/6
		x = ux * ul+px*pixel_l
		y = uy * ul+py*pixel_l
		self.rectangle(x, y, pixel_l, pixel_l, 'black')
	def draw_unit_pixels(self,ux,uy,ul,px1,py1,px2,py2):
		for px in range(px1,px2+1):
			for py in range(py1,py2+1):
				self.draw_unit_pixel(ux,uy,ul,px,py)

	#self.du=draw_unit_c()
	def draw_unit(self,sunit,clean=False):
		#du.draw(x,y,dire)
		global Unit_l
		xoffset = sunit.x * Unit_l
		yoffset = sunit.y * Unit_l
		self.rectangle(xoffset,yoffset,Unit_l,Unit_l,'blue')
		if clean:#clear
			self.unit_list[sunit.x][sunit.y]='e'
		else:
			self.unit_list[sunit.x][sunit.y] = 's'
			if sunit.prev!=None and sunit.next==None:#tail
				if sunit.dire=='N':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 2)
					self.draw_unit_pixel( sunit.x, sunit.y, Unit_l, 3, 3)
				elif sunit.dire=='S':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 3, 3, 5)
					self.draw_unit_pixel( sunit.x, sunit.y, Unit_l, 3, 2)
				elif sunit.dire=='W':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 2, 3)
					self.draw_unit_pixel( sunit.x, sunit.y, Unit_l, 3, 3)
				elif sunit.dire=='E':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 3, 2, 5, 3)
					self.draw_unit_pixel( sunit.x, sunit.y, Unit_l, 2, 3)
			elif sunit.prev==None and sunit.next!=None:#head
				if sunit.dire=='N':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 1, 3, 1)
				elif sunit.dire=='S':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 4)
				elif sunit.dire=='W':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 1, 2, 1, 3)
				elif sunit.dire=='E':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 4, 3)
				self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 2, 3, 3)
				if sunit.next.dire=='N':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 5)
				elif sunit.next.dire=='S':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 1)
				elif sunit.next.dire=='W':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 5, 3)
				elif sunit.next.dire=='E':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 1, 3)
			elif sunit.prev!=None and sunit.next!=None:#body
				if sunit.dire=='N':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 1)
				elif sunit.dire=='S':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 5)
				elif sunit.dire=='W':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 1, 3)
				elif sunit.dire=='E':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 5, 3)
				self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 2, 3, 3)
				if sunit.next.dire=='N':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 4, 3, 5)
				elif sunit.next.dire=='S':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 2, 0, 3, 1)
				elif sunit.next.dire=='W':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 4, 2, 5, 3)
				elif sunit.next.dire=='E':
					self.draw_unit_pixels(sunit.x, sunit.y, Unit_l, 0, 2, 1, 3)

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

class slither_c(room_c):
	def __init__(self,root,x,y,n):
		room_c.__init__(self,root)
		self.head=None
		self.tail=None
		for i in range(n):
			self.append('E',x-i,y)
		p=self.head
		while p!=None:
			self.draw_unit(p)
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
		self.draw_unit(self.head)
		self.draw_unit(self.head.next)
		if food==False:
			self.draw_unit(self.tail,True)
			self.delend()
			self.draw_unit(self.tail)
		return 0
	def change_head_dire(self,dire):
		if (self.head.next.dire=='N'and dire!='S')or \
				(self.head.next.dire == 'S' and dire != 'N') or \
				(self.head.next.dire == 'W' and dire != 'E') or \
				(self.head.next.dire == 'E' and dire != 'W'):
			self.head.dire=dire
			self.draw_unit(self.head)

class game_c(slither_c):
	def __init__(self,root,x,y,n):
		slither_c.__init__(self,root,x,y,n)
		self.game_runing=False
	def game_slither_move(self):
		self.move(False)
		self.Move_after = self.cv.after(800, self.game_slither_move)
	def start_fun(self,event=None):
		if start_botton['text']=='Stop':
			start_botton['text']='Start'
			self.cv.after_cancel(self.Move_after)
			self.game_runing = False
		else:
			start_botton['text'] = 'Stop'
			self.Move_after=self.cv.after(800,self.game_slither_move)
			self.game_runing = True
	def up_fun(self,event):
		#print(event, type(event.keysym))
		if self.game_runing:
			diredict={'w': 'N',		's': 'S',		'a': 'W',		'd': 'E', \
					  'Up': 'N',	'Down': 'S',	'Left': 'W',	'Right': 'E'}
			#print(diredict[event.keysym])
			self.change_head_dire(diredict[event.keysym])
game=game_c(root,20,20,3)

start_botton=tkinter.Button(root,text='Start',command=game.start_fun)
start_botton.place(x=Option_region_x_center,y=30)
root.bind('<space>',game.start_fun)
root.bind('<w>',game.up_fun)
root.bind('<s>',game.up_fun)
root.bind('<a>',game.up_fun)
root.bind('<d>',game.up_fun)
root.bind('<Up>',game.up_fun)
root.bind('<Down>',game.up_fun)
root.bind('<Left>',game.up_fun)
root.bind('<Right>',game.up_fun)
if __name__=='__main__':
	root.mainloop()