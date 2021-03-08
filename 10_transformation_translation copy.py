from py_graphics import *
from time import *

win = GraphWin('GW', 640, 480)

'''-----------------Simple Translation------------------'''
c = Circle(Point(320,240), 20)
c.draw(win)
sleep(1)
c.undraw()
d = Circle(Point(340,260), 20)
d.draw(win)

'''-----------------Auto Translation accross X until the most right boundary------------------'''
# px = 320
# py = 290
# while (px+20) <= win.getWidth():
# 	c = Circle(Point(px,py), 20)
# 	c.draw(win)
# 	sleep(1)
# 	c.undraw()
# 	px += 50

'''-----------------Translation accross X by using mouse------------------'''
# px = 320
# py = 400
# rad = 20
# tf = 50

# while True:
# 	c = Circle(Point(px,py), rad)
# 	c.draw(win)
# 	mp = win.getMouse()
# 	if px > mp.x:
# 		px -= tf
# 	elif px < mp.x:
# 		px += tf
# 	c.undraw()

'''-----------------Translation accross X & Y by using keyboard------------------'''
# px = 22
# py = 22
# rad = 20
# tf = 50
# while True:
# 	c = Circle(Point(px,py), rad)
# 	c.draw(win)
# 	kp = win.getKey()
# 	if kp == 'Escape':
# 		win.close()
# 	elif kp == 'Up' and py-tf > 0:
# 		py -= tf
# 	elif kp == 'Down' and py + tf < win.getHeight():
# 		py += tf
# 	elif kp == 'Left' and px - tf > 0:
# 		px -= tf
# 	elif kp == 'Right' and px + tf < win.getWidth():
# 		px += tf
# 	c.undraw()

win.getMouse()
win.close()