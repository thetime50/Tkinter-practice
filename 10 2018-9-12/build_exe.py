#-*- coding: utf-8 -*-

import os
#build main1 to emmm.exe

out_file_name='emm'
intd=''
intc='c'

if intd=='d':# or input('debug?(d)')=='d':
	print('debug')
	sw = ''
else:
	sw = ' -w'
cmd=os.getenv('PYTHON37')+'\\Scripts\\pyinstaller.exe'+' -F'+sw+' -i .\\img\\emmm.ico .\\main1.py'
cmd+='  --add-data .\\img;.\\img --distpath .\\out  -n '+out_file_name
print(cmd)
os.system(cmd)

if intc=='c' or input('clear more file?(c)')=='c':
	print('clean')
	os.system('rmdir /s /q .\\__pycache__ .\\build')
	os.system('del /s /q .\\'+out_file_name+'.spec')

