#-*- coding： utf-8 -*-

import tkinter
import io
from PIL import Image,ImageTk
import threading
import time
import random


Unit_x_cnt=40
Unit_y_cnt=50
Unit_l=10
Canvas_wide=Unit_x_cnt*Unit_l
Canvas_hight=Unit_y_cnt*Unit_l
Option_region_wide=300
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
		#print(str(self.cv))
		self.unit_list=[['e' for y in range(Unit_y_cnt)] for x in range(Unit_x_cnt)]
		self.slither_cnt=0
		self.food_cnt=0
		self.unit_cnt=Unit_y_cnt*Unit_x_cnt
		self.empty_cnt=self.unit_cnt
		#root.winfo_width()
		#root.winfo_height()
	def __del__(self):
		#print(str(self.cv))
		try:
			self.cv.destroy()
		except:
			pass
		del self.cv
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
	def change_unit_flag(self,x,y,flag):
		if self.unit_list[x][y]!=flag:
			if self.unit_list[x][y]=='e':
				self.empty_cnt-=1
			elif self.unit_list[x][y]=='s':
				self.slither_cnt -= 1
			elif self.unit_list[x][y]=='f':
				self.food_cnt -= 1
			if flag == 'e':
				self.empty_cnt += 1
			elif flag == 's':
				self.slither_cnt += 1
			elif flag == 'f':
				self.food_cnt += 1
			self.unit_list[x][y] =flag
	def draw_unit(self,sunit,clean=False):
		#du.draw(x,y,dire)
		global Unit_l
		xoffset = sunit.x * Unit_l
		yoffset = sunit.y * Unit_l
		self.rectangle(xoffset,yoffset,Unit_l,Unit_l,'#c0c0ff')
		if clean:#clear
			self.change_unit_flag(sunit.x,sunit.y,'e')
		else:
			self.change_unit_flag(sunit.x,sunit.y,'s')
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
	def draw_food(self,x,y):
		self.change_unit_flag(x,y,'f')
		self.draw_unit_pixels(x, y, Unit_l, 2,1,3,2)
		self.draw_unit_pixels(x, y, Unit_l, 2,4,3,4)
		self.draw_unit_pixels(x, y, Unit_l, 1,2,1,3)
		self.draw_unit_pixels(x, y, Unit_l, 4,2,4,3)

	def generate_food(self):
		cnt=0
		ind=random.randrange(self.empty_cnt)
		#t=time.time()
		''''''
		for x in range(Unit_x_cnt):
			for y in range(Unit_y_cnt):
				if self.unit_list[x][y]=='e':
					cnt+=1
					if cnt==ind:
						self.draw_food(x,y)
		''''''
		'''
		x,y=0,0
		while x <Unit_x_cnt:
			y=0
			while y < Unit_y_cnt:
				if self.unit_list[x][y]=='e':
					cnt+=1
					if cnt==ind:
						self.draw_food(x,y)
				y+=1
			x+=1
		'''
		#print((time.time()-t)*1000)

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
		room_c.__del__(self)
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
	def move(self):
		ret=0
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
			ret=-1
		elif self.unit_list[x][y]=='s':
			ret = -1
		else:
			if self.unit_list[x][y]=='e':
				self.draw_unit(self.tail,True)
				self.delend()
				self.draw_unit(self.tail)
				ret=0
			if self.unit_list[x][y] == 'f':
				ret = 1
			self.apphead(self.head.dire, x, y)
			self.draw_unit(self.head)
			self.draw_unit(self.head.next)
		return ret
	def change_head_dire(self,dire):
		if (self.head.next.dire=='N'and dire!='S')or \
				(self.head.next.dire == 'S' and dire != 'N') or \
				(self.head.next.dire == 'W' and dire != 'E') or \
				(self.head.next.dire == 'E' and dire != 'W'):
			self.head.dire=dire
			self.draw_unit(self.head)

tkinter.Label(root,text='Score:',font=("'Helvetica", 15, "bold")).place(x=Option_region_x_center,y=100,anchor=tkinter.CENTER)
Score_number_label=tkinter.Label(root,text='0',font=("'Helvetica", 15, "bold"))
Score_number_label.place(x=Option_region_x_center,y=130,anchor=tkinter.CENTER)

class game_c(slither_c):
	def __init__(self,root,x,y,n):
		#print('12313',dir(self))
		self.root=root
		self.start_x=x
		self.start_y=y
		self.start_n=n
		slither_c.__init__(self,self.root,self.start_x,self.start_y,self.start_n)
		self.game_state='stop'
		self.score=0
		Score_number_label['text'] = str(self.score)
	def __del__(self):
		slither_c.__del__(self)
	def game_slither_move(self):
		ret=self.move()
		if ret<0:
			self.game_state ='died'
			start_botton['text'] = 'Restart'
			self.cv.create_text((Canvas_wide/2,150),text='Game Over',fill='#ffa0a0',\
					font=("'Helvetica", 40, "bold"))
			self.cv.create_text((Canvas_wide/2,150),text='Game Over',fill='#ff0000',\
					font=("'Helvetica", 40, "normal"))
			self.cv.create_text((Canvas_wide / 2, 250), text=str(self.score), fill='#ffa0a0', \
								font=("'Helvetica", 40, "bold"))
			self.cv.create_text((Canvas_wide / 2, 250), text=str(self.score), fill='#ff0000', \
								font=("'Helvetica", 40, "normal"))
		else:
			self.Move_after = self.cv.after(self.move_time, self.game_slither_move)
			if ret>0:
				self.generate_food()
				self.score+=10
				Score_number_label['text']=str(self.score)
	def start_fun(self,event=None):
		if self.game_state == 'run':
			self.game_state = 'stop'
			start_botton['text']='Start'
			self.cv.after_cancel(self.Move_after)
		elif self.game_state == 'stop':
			self.game_state = 'run'
			start_botton['text'] = 'Stop'
			self.Move_after=self.cv.after(self.move_time, self.game_slither_move)
			if self.food_cnt==0:
				self.generate_food()
		else:
			self.__del__()
			self.__init__(self.root, self.start_x, self.start_y, self.start_n)

	def dire_fun(self,event):
		#print(event, type(event.keysym))
		if self.game_state=='run':
			diredict={'w': 'N',		's': 'S',		'a': 'W',		'd': 'E', \
					  'Up': 'N',	'Down': 'S',	'Left': 'W',	'Right': 'E'}
			#print(diredict[event.keysym])
			self.change_head_dire(diredict[event.keysym])
	def set_speed(self,speed):
		self.move_time=820-int(speed)*10
game=game_c(root,20,20,3)

start_botton=tkinter.Button(root,text='Start',command=game.start_fun)
start_botton.place(x=Option_region_x_center,y=30,anchor=tkinter.CENTER)
root.bind('<space>',game.start_fun)
root.bind('<w>',game.dire_fun)
root.bind('<s>',game.dire_fun)
root.bind('<a>',game.dire_fun)
root.bind('<d>',game.dire_fun)
root.bind('<Up>',game.dire_fun)
root.bind('<Down>',game.dire_fun)
root.bind('<Left>',game.dire_fun)
root.bind('<Right>',game.dire_fun)

scale = tkinter.Scale(root, from_=0, to=80, length=200, orient=tkinter.HORIZONTAL, command=game.set_speed)
scale.set(30)
scale.place(x=Option_region_x_center, y=230, anchor=tkinter.CENTER)

if __name__=='__main__':
	root.mainloop()