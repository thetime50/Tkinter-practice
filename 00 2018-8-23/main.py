#-*- coding: utf-8 -*-
from tkinter import *

root = Tk()
li=['123','456','abc']
li2=['aaa','bbb','ccc','dddd']
listb=Listbox(root)		#创建列表
listb2=Listbox(root)
for i in li:
	listb.insert(0,i)	#添加数据
for i in li2:
	listb2.insert(0,i)
listb.pack()			#列表加入窗口
listb2.pack()

bu=Button(root,text='Button')
class Crgb:
	def __init__(self):
		self.i=0
		self.j=0
	def fun(self):
		step=9
		self.j=(self.j+1)%step
		if self.j==0: self.i=(self.i+1)%3
		li=[0,0,0]
		#li[self.i]=0
		li[(self.i+1)%3]=(step-self.j)*8
		li[(self.i+2)%3]=self.j*8
		col='#%x%x%x'%(0xff-li[0],0xff-li[1],0xff-li[2])
		bu['bg'] =col
		listb['bg'] =col
		#bu['state'] =DISABLED
		return

rgb=Crgb()
bu['bg']='#a0ffff'
bu['highlightcolor']=bu['bg']
bu['command']=rgb.fun
print(bu['activebackground'])

bu.pack()
root.mainloop()
