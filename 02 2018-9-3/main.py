#-*- coding: utf-8 -*-
import tkinter
TK=tkinter
root=TK.Tk()
root.wm_title('window')
root.wm_minsize(300,200)

l1=TK.Label(root)
l1['text']='hello world'
l2=TK.Label(root,text='l1 hello world',background='#a0ffff' )

l1.pack()
l2.pack()


class ad_lable:
	s=[]
	def add_lable(self):
		global root
		self.s.append(TK.Label(root,text='add '+str(len(self.s)+1)))
		self.s[-1].pack()
	def del_lable(self):
		if(len(self.s)):
			self.s[-1].pack_forget()#.grid_forget()#这样无效
			self.s.pop(-1)
ad=ad_lable()
b1=TK.Button(root,text='add label',command=ad.add_lable)
b1.pack()#这里这是注册用的
#del b1#没有变化

b2=TK.Button(root,text='del label',command=ad.del_lable)
b2.pack()

def b3_fun(event):
	global b3
	b3['text'] = event
def b3_func(event):
	global b3
	b3['text'] = b3['text']+' func'

b3=TK.Button(root,text='b3')
b3.bind('<Button-1>',b3_fun)#<Alt-Button-1>也会进来
b3.bind('<Button-1>',b3_func,add=True)
b3.bind('<Control-Button-1>',b3_fun)
b3.bind('<Alt-A>',b3_fun)#????
b3.pack()

b4=TK.Button(root,text='b4',width='20',height='2',background='#a0ffa0')
b4.pack()

root.mainloop()