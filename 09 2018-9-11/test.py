from main import *
stest1=slither_unit_c(10,10,'N')
stest2=slither_unit_c(10,11,'S',stest1)
stest1.next=stest2
draw_unit(stest1)
draw_unit(stest2)
stest1.x+=1
stest2.x+=1
stest1.dire='S'
stest2.dire='N'
draw_unit(stest1)
draw_unit(stest2)
stest1.x+=1
stest2.x+=1
stest1.dire='W'
stest2.dire='E'
draw_unit(stest1)
draw_unit(stest2)
stest1.x+=1
stest2.x+=1
stest1.dire='E'
stest2.dire='W'
draw_unit(stest1)
draw_unit(stest2)

xoffset = 30 * Unit_l
yoffset = 40 * Unit_l
rectangle(xoffset, yoffset, Unit_l, Unit_l, 'blue')
draw_unit_pixel(30,40,Unit_l,0,1)
slither=slither_c(20,20,3)
slither.head.dire='N'
slither.move(True)
slither.head.dire='W'
slither.move(True)
slither.head.dire='W'
slither.move(True)
slither.head.dire='W'
slither.move(True)
slither.head.dire='S'
slither.move(True)
slither.head.dire='S'
slither.move(True)
slither.head.dire='S'
slither.move(True)
slither.head.dire='E'
slither.move(True)
slither.head.dire='E'
slither.move(True)
slither.head.dire='E'
slither.move(True)
slither.head.dire='S'
slither.move(True)
slither.head.dire='S'
slither.move(True)
slither.head.dire='S'
slither.move(True)
slither.head.dire='W'
slither.move(True)
slither.head.dire='W'
slither.move(True)
slither.head.dire='W'
slither.move(True)
slither.head.dire='N'
slither.move(True)
slither.head.dire='E'
slither.move(True)
slither.head.dire='E'
slither.move(False)

if __name__=='__main__':
	root.mainloop()

