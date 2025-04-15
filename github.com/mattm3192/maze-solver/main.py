from graphics import *

def main():
	win = Window(800, 600)
	p1 = Point(10, 30)
	p2 = Point(140, 150)
	p3 = Point(400, 300)
	p4 = Point(240,150)
	l1 = Line(p1, p2)
	l1.draw(win.canvas)
	l2 = Line(p3, p4)
	l2.draw(win.canvas, "red")
	l3 = Line(p1, p3)
	l3.draw(win.canvas, "blue")

	win.wait_for_close()

main()