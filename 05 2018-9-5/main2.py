#-*- coding: utf-8 -*-
from tkinter import *
## 文本 ##
root=Tk()
root.update()
#print(root.winfo_x()/2)
t=Text(root,width=52)

tm=Menu(t,tearoff = 0)
def tm_save():
	global t
	print('\'',t.get("0.0", "end"),'\'')#只提取出字符部分
tm.add_command(label='Save',command=tm_save)
def t_rclick(event):
	global tm
	tm.post(event.x_root,event.y_root)
t.bind('<Button-3>',t_rclick)
t.pack(side=LEFT,fill=BOTH)
bu_arr=[]
def bu_fun():
	global t,bu_arr
	s='Button '+str(len(bu_arr)+1)
	print(s)
	bu_arr.append(Button(t,text=s,command=bu_fun))
	t.window_create(INSERT,window=bu_arr[-1])

bu=Button(t,text='Button',command=bu_fun)
t.window_create(INSERT,window=bu)

cv=Canvas(root,width=400,bg='white')
cv.create_line((10,10),(30,50),width=2)
cv.create_line((2,2),(30,50),width=2)
cv.create_arc((60,60),(90,90))
bcv_str=''
def bcv_fun(event):
	global cv,bcv_str
	#cv.create_text((200, 100), text=bcv_str,fill='white')
	cv.create_rectangle((2,90),(400,110),fill='white')
	bcv_str=str(event)
	cv.create_text((200, 100), text=bcv_str)
cv.bind('<Button-1>',bcv_fun)

cv.pack(side=LEFT,fill=BOTH)
t.mainloop()