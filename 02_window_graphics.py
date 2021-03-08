from py_graphics import *

win = GraphWin('Computer Graphics', 640, 480)
win.setBackground(color_rgb(0, 0, 0))

# your code here

win.getMouse()
win.close()

'''
To close the window with confirmation you can use

    win.getMouse()      # Pause to view result
    win.close()         # Close window when done
        OR
    win.promptClose(x, y)       # x & y are coordinates to which the default exit message will be displayed
        OR
    win.promptMouse(x, y, "Your custom message here")       # with custom message

'''
