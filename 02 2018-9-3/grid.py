#-*- coding: utf-8 -*-
import tkinter
TK=tkinter

root=TK.Tk()
TK.Label(root,text='User:').grid(row=0,sticky=TK.W)
TK.Entry(root).grid(row=0,column=1,sticky=TK.W)

TK.Label(root,text='Pass:').grid(row=1,sticky=TK.W)
TK.Entry(root).grid(row=1,column=1,sticky=TK.E)

TK.Button(root,text='Sing in').grid(row=2,column=0,columnspan=2)

root.mainloop()