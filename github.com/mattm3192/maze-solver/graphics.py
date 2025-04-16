from tkinter import Tk, BOTH, Canvas

class Window:
	def __init__(self, width, height):
		self.__root = Tk()
		self.__root.title("Maze Solver")
		self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
		self.canvas.pack(fill=BOTH, expand=1)
		self.__running = False
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
	
	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()

	def wait_for_close(self):
		self.__running = True
		while self.__running:
			self.redraw()
		print("window closed...")

	def close(self):
		self.__running = False

	def draw_line(self, line, fill_color="black"):
		line.draw(self.canvas, fill_color)


class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

class Line():
	def __init__(self, point1, point2):
		self.__point1 = point1
		self.__point2 = point2
	
	def draw(self, canvas, fill_color="black"):
		canvas.create_line(
			self.__point1.x, self.__point1.y, self.__point2.x, 
			self.__point2.y, fill=fill_color, width=2
			)

class Cell():
	def __init__(self, window):
		self.window = window
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self._x1 = 0
		self._x2 = 0
		self._y1 = 0
		self._y2 = 0
		self._win = False

	def draw(self, x1, y1, x2, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		top_wall = Line(Point(x1, y1), Point(x2, y1))
		left_wall = Line(Point(x1, y1), Point(x1, y2))
		right_wall = Line(Point(x2, y1), Point(x2, y2))
		bottom_wall = Line(Point(x1, y2), Point(x2, y2))

		if self.has_bottom_wall:
			bottom_wall.draw(self.window.canvas)
		if self.has_left_wall:
			left_wall.draw(self.window.canvas)
		if self.has_right_wall:
			right_wall.draw(self.window.canvas)
		if self.has_top_wall:
			top_wall.draw(self.window.canvas)
	