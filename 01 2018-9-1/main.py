#-*- coding: utf-8 -*-
import tkinter
TK=tkinter
import math
'''for n in range(2,10):
	li=[str(x)*x for x in range(1,n) for y in range(3)]
	put_list((li))
	print('')
'''
def put_list(li,n=3):
	tablen=4
	cnt=0
	lens=[len(i) for i in li]
	maxlen=max(lens)
	wide=math.ceil((maxlen+2+1)/tablen)
	for i in li:
		print('\''+str(i)+'\'',end='')
		print('	'*(wide-(len(i)+2)//tablen),end='')
		cnt+=1
		if cnt%n==0:
			print('')
#
#put_list(dir(tkinter))
root=TK.Tk()
root.wm_title('tk test window')
#put_list(dir(root))
root.minsize(300,150)
root.maxsize(800,400)

lab=TK.Label(root,text='test text')
put_list(dir(lab))

lab1=TK.Label(root)
lab1['text']='lab1 text test'

lab.pack()
lab1.pack()
root.mainloop()
