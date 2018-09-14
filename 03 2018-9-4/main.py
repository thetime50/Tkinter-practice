#-*- coding: utf-8 -*-
import tkinter
TK=tkinter
root=TK.Tk()
TK.Label(root,text='User:').grid(row=0,column=0)
TK.Label(root,text='Pass:').grid(row=1,column=0)
lu=TK.Entry(root)
lp=TK.Entry(root)
lu.grid(row=0,column=1)
lp.grid(row=1,column=1)

def sing_fun():
	global lu,lp,li
	if lu.get()=='User' and lp.get()=='Pass':
		li['text']='Sign in ok'
		li['foreground']='green'
	else:
		li['text']='User or Pass error'
		li['foreground']='red'
TK.Button(text='Sign in',command=sing_fun).grid(row=2,column=0,columnspan=2)
li=TK.Label(text='Please entry')
li.grid(row=3,column=0,columnspan=2)

## menu ###
menubar=TK.Menu(root)
fmenu=TK.Menu(menubar)
for iten in ['新建','打开','保存','另存为']:
	fmenu.add_command(label=iten)#command=fun
emenu=TK.Menu(menubar)
for iten in ['复制','剪切','黏贴']:
	emenu.add_command(label=iten)
vmenu=TK.Menu(menubar)
for iten in ['默认视图','自定义...']:
	vmenu.add_command(label=iten)
amenu=TK.Menu(menubar)
for iten in ['帮助','关于']:
	amenu.add_command(label=iten)

for name,menu in[('文件',fmenu),('编辑',emenu),('视图',vmenu),('帮助',amenu)]:
	menubar.add_cascade(label=name,menu=menu)


menubar.add_command(label='test1')

'''
t2menu=TK.Menu(menubar)
for iten in ['11','222','333']:
	t2menu.add_command(label=iten)
menubar.add_command(label='test2',menu=t2menu)#这样是不行的
'''
t3menu=TK.Menu(menubar)
t31menu=TK.Menu(t3menu)
#t31menu=TK.Menu(menubar)#不知道这里写错有什么影响
for iten in ['1-11','1-222','1-333']:
	t31menu.add_command(label=iten)

t3menu.add_cascade(label='t3-1',menu=t31menu)
for iten in ['11','222','333']:
	t3menu.add_command(label=iten)
t3menu.add_separator()
t3menu.add_command(label='separator')
menubar.add_cascade(label='test3',menu=t3menu)

root['menu']=menubar

#右键菜单
rcmenu=TK.Menu(root)
for iten in ['剪切','复制','黏贴','撤销','重复']:
	rcmenu.add_command(label=iten)
def rclick_fun(event):
	rcmenu.post(event.x_root,event.y_root)

root.bind('<Button-3>',rclick_fun)

ccmenu=TK.Menu(root)
for iten in range(4):
	ccmenu.add_checkbutton(label=str(iten)*2)
ccmenu.add_separator()
for iten in range(4,8):
	ccmenu.add_radiobutton(label=str(iten)*2)#和分割线无关,只能有一项被选中
ccmenu.add_separator()
for iten in range(8,12):
	ccmenu.add_checkbutton(label=str(iten)*2)
ccmenu.add_separator()
for iten in range(12,16):
	ccmenu.add_radiobutton(label=str(iten)*2)#

def cclick_fun(event):
	ccmenu.post(event.x_root,event.y_root)
root.bind('<Button-2>',cclick_fun)

##对话框
import tkinter.dialog
Dlog=tkinter.dialog
dl=TK.Label(text='Dialog')
dl.grid(row=4,column=1)
def make_dlog():
	d=Dlog.Dialog(None,title='Dialog',text='反正一切来不及',bitmap=Dlog.DIALOG_ICON,default=0,strings=('1','2','3','4'))
	dl['text']=d.num
	dl['foreground']='#b0b000'
	print(d.num)
mdlogb=TK.Button(root,text='Dialog',command=make_dlog)#这里的root改为None好像效果一样
mdlogb.grid(row=4)
qdlogb=TK.Button(root,text='Close Dialog',command=mdlogb.quit)#为什么窗口退出了
qdlogb.grid(row=5)

root.mainloop()

