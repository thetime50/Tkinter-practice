#-*- coding: utf-8 -*-

import os
#build main1 to emmm.exe

intd='d'
intc='c'

if intd=='d' or input('debug?(d)')=='d':
	print('debug')
	sw = ''
else:
	sw = ' -w'
cmd=os.getenv('PYTHON37')+'\\Scripts\\pyinstaller.exe'+' -F'+sw+' -icon .\\img\\emmm.ico .\\main1.py'
print(cmd)
os.system(cmd)

if intc=='c' or input('clear more file?(c)')=='c':
	print('clean')

