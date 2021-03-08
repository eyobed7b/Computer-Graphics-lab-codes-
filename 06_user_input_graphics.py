from py_graphics import *

win = GraphWin('GW', 640, 480)

tF = Entry(Point(320, 200), 10)
tF.draw(win)
tB = Text(Point(320,230),'')
tB.draw(win)
while True:
    kp = win.getKey()
    if kp == 'Escape':
        win.close()
    else:
        tB.setText(tF.getText())

win.getMouse()
win.close()