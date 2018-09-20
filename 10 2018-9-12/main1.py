#-*- conding: utf-8 -*-

import tkinter,tkinter.filedialog
import PIL.Image,PIL.ImageTk,PIL.ImageGrab
import math
import sys
import win32con,win32clipboard
from io import BytesIO
#import windnd

#import io.StringIO

win_width=600
win_high=400

if getattr(sys, 'frozen', False):  # 是否Bundle Resource
	base_path = sys._MEIPASS
else:
	base_path = '.'
icon_path=base_path+'\\img\\emmm.ico'
emm_path=base_path+'\\img\\timg.png'
root=tkinter.Tk()
root.title('emmmm')
root.iconbitmap(icon_path)
root.minsize(win_width,win_high)
win_x=int((root.winfo_screenwidth()-win_width)*0.382)
win_y=int((root.winfo_screenheight()-win_high)*0.382)
#print('+%s+%s'%(str(win_x),str(win_y)))
root.geometry('+%s+%s'%(str(win_x),str(win_y)))

#cv=tkinter.Canvas(root,width=win_width,heigh=win_high,bg='white')
cv=tkinter.Canvas(root,bg='white')

######Draw###################################
class DrawImageClass:
	img = PIL.Image.open(emm_path)
	tkimg = lambda self, w, h: PIL.ImageTk.PhotoImage(self.img.resize((w, h), PIL.Image.ANTIALIAS))

	init_w=30
	init_h=30
	def __init__(self):
		self.puten=False
		self.motion_cnt=0
		self.press_cnt = 0
		self.release_cnt = 0
		self.w,self.h=self.limtit_wh(self.img.width,self.img.height,self.init_w,self.init_h)
		self.image =[]
		self.checked=False
		self.ctrl = False
	def limtit_wh(self,w,h,limit_w,limit_h):
		trans_w,trans_h=limit_w,limit_h
		if w/h > limit_w/limit_h:
			trans_w = limit_w
			trans_h = int(h * limit_w / w)
		else:
			trans_w = int(w * limit_h / h)
			trans_h = limit_h
		if trans_w==0:trans_w=1
		if trans_h==0:trans_h=1
		return trans_w,trans_h

	def draw(self):
		if self.ctrl:
			w,h=self.limtit_wh(self.img.width,self.img.height,self.w,self.h)
		else:
			w=self.w
			h=self.h
		self.image[-1]=self.tkimg(w, h)
		cv.create_image(self.x, self.y, image=self.image[-1], anchor=tkinter.CENTER)
	def B1Press_fun(self,event):
		self.press_cnt+=1
		if self.puten: print('bpress',str(event),self.press_cnt)

		self.checked =True
		self.resize=False
		self.x=event.x
		self.y=event.y
		self.image.append(self.tkimg(self.w, self.h))
		cv.create_image(self.x, self.y, image=self.image[-1], anchor=tkinter.CENTER)

	def B1Motion_fun(self,event):
		self.motion_cnt+=1
		if self.puten: print('bmotion',str(event),self.motion_cnt)

		if abs(event.x - self.x) * 2 > self.w or self.resize:
			self.resize = True
			self.w = math.ceil(abs(event.x - self.x)*2)
			if self.w < 1: self.w = 1
		if abs(event.y - self.y) * 2 > self.h or self.resize:
			self.resize = True
			self.h = math.ceil(abs(event.y - self.y)*2)
			if self.h<1:self.h=1
		self.draw()
		# print(self.x, self.y,event.x, event.y,self.w, self.h)

	def B1Release_fun(self,event):
		self.release_cnt+=1
		if self.puten: print('brelease',str(event),self.release_cnt)

		self.checked =False
		#del self.image[-1]
	def CPress_fun(self,event):
		del self.image
		self.image = []
	def CtlPress_fun(self,event):
		self.ctrl = True
		if self.checked:
			self.draw()
	def CtlRelease_fun(self,event):
		self.ctrl=False
		if self.checked:
			self.draw()
	def Ctl_z_fun(self,event):
		if len(self.image):
			del self.image[-1]
	def Ctl_c_fun(self,event):
		if 'win' in sys.platform:
			points = (cv.winfo_rootx(), cv.winfo_rooty(), cv.winfo_rootx() + cv.winfo_width(),
					  cv.winfo_rooty() + cv.winfo_height())
			img = PIL.ImageGrab.grab(points)
			output = BytesIO()
			img.convert("RGB").save(output, "BMP")
			data = output.getvalue()[14:]
			output.close()
			win32clipboard.OpenClipboard()
			win32clipboard.EmptyClipboard()
			win32clipboard.SetClipboardData(win32con.CF_DIB, data)
			win32clipboard.CloseClipboard()
	def Ctl_v_fun(self,event):
		im=PIL.ImageGrab.grabclipboard()
		if not im:
			try:
				win32clipboard.OpenClipboard()
				name = win32clipboard.GetClipboardData(win32con.CF_HDROP)
				win32clipboard.CloseClipboard()
				print(name)
				im = PIL.Image.open(name[0])
			except:
				return
		if im:
			self.img = im
			self.w,self.h=self.limtit_wh(im.width,im.height,self.init_w,self.init_h)
	def Ctl_r_fun(self,event):
		self.img = PIL.Image.open(emm_path)
		self.w,self.h=self.limtit_wh(self.img.width,self.img.height,self.init_w,self.init_h)
	'''def drop_fun(self,flist):
		for idx, i in enumerate(flist):
			print(idx, i)'''

	def Ctl_s_fun(self,event):
		name=tkinter.filedialog.asksaveasfilename(defaultextension='.jpg',filetypes=[('PNG', '.png'), ('JPG', '.jpg')])
		if name:
			points=(cv.winfo_rootx(),cv.winfo_rooty(),cv.winfo_rootx()+cv.winfo_width(),cv.winfo_rooty()+cv.winfo_height())
			img=PIL.ImageGrab.grab(points)
			img.save(name)
	def __del__(self):
		print('__del__')

DrawImage=DrawImageClass()

cv.bind('<B1-Motion>',DrawImage.B1Motion_fun)
cv.bind('<Button-1>',DrawImage.B1Press_fun)
cv.bind('<ButtonRelease-1>',DrawImage.B1Release_fun)
root.bind('<c>',DrawImage.CPress_fun)
root.bind('<Shift_L>',DrawImage.CtlPress_fun)
root.bind('<KeyRelease-Shift_L>',DrawImage.CtlRelease_fun)
root.bind('<Control-z>',DrawImage.Ctl_z_fun)
root.bind('<Control-c>',DrawImage.Ctl_c_fun)
root.bind('<Control-v>',DrawImage.Ctl_v_fun)
root.bind('<Control-r>',DrawImage.Ctl_r_fun)
#windnd.hook_dropfiles(root,func=DrawImage.drop_fun)

root.bind('<Control-s>',DrawImage.Ctl_s_fun)

cv.pack(fill=tkinter.BOTH, expand=True)
root.mainloop()
