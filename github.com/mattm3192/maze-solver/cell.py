from graphics import Line, Point


class Cell():
	def __init__(self, window):
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self._x1 = 0
		self._x2 = 0
		self._y1 = 0
		self._y2 = 0
		self._window = window

	def draw(self, x1, y1, x2, y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

		if self.has_bottom_wall:
			line = Line(Point(x1, y2), Point(x2, y2))
			self._window.draw_line(line)
		if self.has_left_wall:
			line = Line(Point(x1, y1), Point(x1, y2))
			self._window.draw_line(line)
		if self.has_right_wall:
			line = Line(Point(x2, y1), Point(x2, y2))
			self._window.draw_line(line)
		if self.has_top_wall:
			line =Line(Point(x1, y1), Point(x2, y1))
			self._window.draw_line(line)
	