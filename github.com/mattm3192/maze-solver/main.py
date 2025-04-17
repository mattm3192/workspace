from graphics import *
from cell import *

def main():
	win = Window(800, 600)
	cell1 = Cell(win)
	#cell1.has_right_wall = False
	cell2 = Cell(win)
	#cell2.has_left_wall = False
	#cell2.has_bottom_wall = False
	cell3 = Cell(win)
	#cell3.has_top_wall = False
	#cell3.has_right_wall = False

	cell1.draw(1, 1, 100, 100)
	cell2.draw(50, 1, 50, 100)
	cell3.draw(100, 100, 200, 200)

	win.wait_for_close()

main()