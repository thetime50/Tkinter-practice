#-*- coding: utf-8 -*-
import tkinter
TK=tkinter

root=TK.Tk()
cnt=0
def l1_fun(event):
	global cnt,l1
	cnt+=1
	l1['text']='li '+str(cnt)

l1=TK.Label(root,text='l1')
l1.bind('<Button-1>',l1_fun)

def l2_fun(event):
	global l2
	l2['text']=event
l2=TK.Label(root,text='l2')
l2.bind_all(l2_fun)#????

def l3_fun(event):
	global l3
	l3['text']=event
l3=TK.Label(root,text='l3')
l3.bind_class('Entry','Control',l3_fun)#???

def l4_fun(event):
	global l1,l4
	l1.unbind('<Button-1>')
	l4['text']='l1 unbind'
l4=TK.Label(root,text='l4')
l4.bind('<Button-1>',l4_fun)#???

l1.pack()
l2.pack()
l3.pack()
l4.pack()

#root.overrideredirect(1)
root.mainloop()