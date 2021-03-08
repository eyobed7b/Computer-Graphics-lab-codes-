from py_graphics import *

win = GraphWin('GW', 640, 480)

''' Get Keyboard Input '''
t = Text(Point(310,210),'')
t.draw(win)
while True:
    kp = win.getKey()
    
    if kp == 'Escape':
        win.close()
    else:
        t.setText('You pressed ' + str(kp))
        
win.getMouse()
win.close()