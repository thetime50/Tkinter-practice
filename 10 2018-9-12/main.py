#-*- conding: utf-8 -*-

import tkinter
import PIL.Image,PIL.ImageTk

root=tkinter.Tk()
cv=tkinter.Canvas(root,width=600,heigh=400,bg='white')
#cv.place(x=0,y=0)

img=PIL.Image.open('./img/timg.jpg')
tkimg=lambda w,h:PIL.ImageTk.PhotoImage(img.resize((w,h),PIL.Image.ANTIALIAS))
bimage=tkimg(10,10)
b_cvimage=cv.create_image(200,200,image=bimage,anchor=tkinter.CENTER)
aimage=tkimg(100,100)
cv.create_image(200,200,image=aimage,anchor=tkinter.SE)#是参考点相对于图片的方位

def ca_but():
	global aimage
	aimage=tkimg(300,100)#变没掉了
	print(type(aimage))
change_a_butt=tkinter.Button(text='change img a',command=ca_but)
def db_but():
	global b_cvimage
	print(type(b_cvimage))#没有用
	del b_cvimage
del_b_cvimage_butt=tkinter.Button(text='del b cv.create_image',command=db_but)

cv.pack()
change_a_butt.pack()
del_b_cvimage_butt.pack()
root.mainloop()
