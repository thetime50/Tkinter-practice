#-*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *

import inspect
import sys

def get_current_function_name():
    return inspect.stack()[1][3]
def get_current_function_name1():
    return sys._getframe().f_back.f_code.co_name

def gcfn():
    return inspect.stack()[1][3]

root=Tk()
root.title('消息框')
root.minsize(300,200)

la=Label(root,text='message',foreground='#ff2020')
la.pack()
def bsifun():
	la['text'] =gcfn()+' '+showinfo(title='showinfo',message='hello')
Button(root,text='message',command=bsifun).pack()

def bswfun():
	la['text'] =gcfn()+' '+showwarning(title='showwarning',message='warning')
Button(root,text='warning',command=bswfun).pack()

def bsefun():
	la['text'] =gcfn()+' '+showerror(title='showerror',message='error')
Button(root,text='error',command=bsefun).pack()

def baqfun():
	la['text']=gcfn()+' '+askquestion(title='askquestion',message='question')
Button(root,text='question',command=baqfun).pack()

def baofun():
	la['text']=gcfn()+' '+str(askokcancel('askokcancel','okcancel'))
Button(root,text='okcancel',command=baofun).pack()

def bynfun():
	la['text']=gcfn()+' '+str(askyesno('askyesno','yesno'))
Button(root,text='yesno',command=bynfun).pack()

def byncfun():
	la['text']=gcfn()+' '+str(askyesnocancel('askyesnocancel','yesnocancel'))
Button(root,text='yesnocancen',command=byncfun).pack()

def brcfun():
	la['text']=gcfn()+' '+str(askretrycancel('askretrycancel','retrycancel'))
Button(root,text='retrycancel',command=brcfun).pack()

root.mainloop()