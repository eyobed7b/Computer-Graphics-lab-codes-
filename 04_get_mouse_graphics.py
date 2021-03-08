from py_graphics import *

win = GraphWin('GW', 640, 480)

''' Get Mouse Input '''
t = Text(Point(320,220),'')
t.draw(win)
while True:
    mp = win.getMouse()
    t.setText('You clicked @ ' + str(mp.x) + '  ' + str(mp.y))

win.getMouse()
win.close()