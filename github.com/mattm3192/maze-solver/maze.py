from cell import Cell


class Maze():
	def __init__(self, x1, y1, num_rows, num_cols, 
			  cell_size_x, cell_size_y, window			  
			  ):
		self._x1 = x1
		self._y1 = y1
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._window = window
		self._cells = []
		self._create_cells()

	def _creat_cells(self):
		for i in range(self._num_cols):
			row = []
			for j in range(self._num_rows):
				row[j] = Cell(self._window)
			self._cells[i] = row

		for i in range(self._num_cols):
			for j in range(self._num_rows):
				self._draw_cell(i, j)

	def _draw_cell(self, i, j):
		pass