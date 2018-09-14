#-*- coding： utf-8 -*-

import tkinter
import io
from PIL import Image,ImageTk
import threading


Unit_x_cnt=100
Unit_y_cnt=80
Unit_l=6
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
	unit_img={Image.open('./img/'+x).resize(Unit_l,Unit_l) 	for x in\
		['empty','food',\
		'head_N','head_S','head_W','head_E', \
		'pear_N','pear_S','pear_W','pear_E', \
		'body_NE', 'body_SE', 'body_SW', 'body_NW', 'body_NS', 'body_WE']}

	def draw(self,x,y,sr):
		global cv,Unit_l
		#cv.create_image(x*Unit_l,y*Unit_l,image=self.unit_img[sr])

du=draw_unit_c()
def draw_unit(x,t,sr):
	du.draw(x,y,sr)

'''
time task
	delay
	food? slither head ++ draw
	slither++ del end draw
	new food draw
'''
'''
key task
	wait key
	slither head change dir draw
'''
root.mainloop()