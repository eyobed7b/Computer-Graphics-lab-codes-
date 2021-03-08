from py_graphics import *

win = GraphWin('GW', 640, 480)

''' Point Drawing '''
pt = Point(10, 30)
pt.setOutline(color="red")
pt.draw(win)


''' Line Drawing '''
ln = Line(Point(15,10), Point(150,10))
ln.setOutline(color_rgb(200,100,0))
ln.setWidth(5)
ln.draw(win)

''' Rectangle Drawing '''
rc = Rectangle(Point(100,10), Point(140,70))
rc.setOutline(color_rgb(8,8,100))
rc.setWidth(5)
rc.setFill(color_rgb(255,100,50))
rc.draw(win)

''' Circle Drawing '''
ci = Circle(Point(220,60), 50)
ci.setOutline(color="red")
ci.setFill(color="brown")
ci.draw(win)

''' Oval Drawing '''
ov = Oval(Point(300,60), Point(400,90))
ov.setFill(color="light blue")
ov.draw(win)

''' Pieslice Drawing '''
ci = Pieslice(Point(450,60), Point(550,120), 0, 250)
ci.setFill(color="red")
ci.draw(win)

''' Arc Drawing '''
ci = Arc(Point(50,200), Point(90,250), 0, 250)
ci.setFill(color="red")
ci.draw(win)

''' Chord Drawing '''
ci = Chord(Point(120,200), Point(190,270), 0, 250)
ci.setFill(color="red")
ci.draw(win)

''' Polygon Drawing '''
pl = Polygon(Point(230,200), Point(290,200), Point(290,100),Point(230,100))
pl.setFill(color="yellow")
pl.draw(win)

''' Polygon Drawing 2 '''
pts = [Point(330,200),  Point(390,240), Point(350,300), Point(310,300)]
pl2 = Polygon(pts)
pl2.setOutline(color_rgb(8,8,100))
pl2.setWidth(0)
pl2.setFill(color="Green")
pl2.draw(win)

''' Text Displaying 1'''
Text(Point(100,400),'this is test').draw(win)

''' Text Displaying 2'''
tx = Text(Point(230, 400),'This is test 2')
tx.setTextColor(color='DARK BLUE')
tx.setText('This is test 3')
tx.setSize(17)
tx.setFace('arial')
tx.draw(win)

''' Image Displaying '''
Image(Point(350, 400),"flutter.png").draw(win)

win.getMouse()
win.close()