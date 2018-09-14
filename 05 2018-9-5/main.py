#-*- coding: utf-8 -*-
from tkinter import *
#from tkinter.ttk import * #win风格的界面

## 控件 ##
root=Tk()
l1=Label(root,text='None',foreground='green')
def cb_fun():#没有event参数的
	global l1,v1,v2,sv1,sv2
	l1['text']='%s %s'%(str(v1.get()),str(v2.get()))
	#没有cb1.get()的
	print(v1.get())
	sv1.set('Checkbutton1-1' if v1.get() else 'Checkbutton1-0')
	sv2.set('Checkbutton2-1' if v2.get() else 'Checkbutton2-0')
v1,v2=IntVar(),IntVar()#真鸡儿麻烦
sv1,sv2=StringVar(),StringVar()#什么用处呢?
sv1.set('Checkbutton1-1' if v1.get() else 'Checkbutton1-0')
sv2.set('Checkbutton2-1' if v2.get() else 'Checkbutton2-0')
cb1=Checkbutton(root,text='Checkbutton1',variable=v1,textvariable=sv1,command=cb_fun)
cb2=Checkbutton(root,text='Checkbutton2',variable=v2,textvariable=sv2,command=cb_fun)
cb1.pack()
cb2.pack()
l1.pack()

l2=Label(root,text='None',foreground='green')
def rb_fun():
	global l2,v3
	l2['text']=str(v3.get())
v3=IntVar()
Radiobutton(root,text='Radiobutton1',variable=v3,value=1,command=rb_fun).pack()#value相当于是case
Radiobutton(root,text='Radiobutton2',variable=v3,value=2,command=rb_fun).pack()
Radiobutton(root,text='Radiobutton3',variable=v3,value=3,command=rb_fun).pack()
Radiobutton(root,text='Radiobutton4',variable=v3,value=4,command=rb_fun).pack()
l2.pack()

l3=Label(root,text='None',foreground='green')
def rb1_fun():
	global l3,v4
	l3['text']=str(v4.get())
v4=IntVar()
Radiobutton(root,text='Radiobutton5',variable=v4,value=1,command=rb1_fun).pack()#value相当于是case
Radiobutton(root,text='Radiobutton6',variable=v4,value=2,command=rb1_fun).pack()
Radiobutton(root,text='Radiobutton7',variable=v4,value=3,command=rb1_fun).pack()
l3.pack()

root.mainloop()



