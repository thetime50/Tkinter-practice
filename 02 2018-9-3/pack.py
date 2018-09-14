#-*- coding: utf-8 -*-
import tkinter
TK=tkinter

root=TK.Tk()
TK.Button(root,text='A').pack(side=TK.RIGHT)
TK.Button(root,text='B').pack(fill=TK.X)
TK.Button(root,text='C').pack(expand=TK.NO)
TK.Button(root,text='C1').pack(expand=TK.NO)
TK.Button(root,text='C3').pack(expand=TK.YES)#平均的效果
TK.Button(root,text='C3').pack(expand=TK.YES)
TK.Button(root,text='D').pack(anchor=TK.SW)
TK.Button(root,text='D1').pack(anchor=TK.SW)

TK.Button(root,text='E').pack(ipadx=30)
TK.Button(root,text='F').pack(ipady=30)
TK.Button(root,text='G').pack(padx=30)
TK.Button(root,text='H').pack(pady=30)




root.mainloop()