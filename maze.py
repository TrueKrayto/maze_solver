from cell import Cell
from graphics import Window
import time

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win,):
        self.x1 = x1
        self.y1 = y1
        self.rows = num_rows
        self.cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
    
    def create_cells(self):
        all_cells = []
        for col in range(self.cols):
            col = []
            for row in range(self.rows):
                cell = Cell(self.win)
                col.append(cell)
            all_cells.append(col)
        self.cells = all_cells
        for i in range(len(self.cells[0])):
            for j in range(len(self.cells)):
                pos = self._draw_cell(j, i)
                cell = self.cells[j][i]
                cell.draw(*pos)
                self._animate()

    def _draw_cell(self, j, i):
        x1 = (j * self.cell_size_x) + self.x1
        x2 = x1 + self.cell_size_x
        y1 = (i * self.cell_size_y) + self.y1
        y2 = y1 + self.cell_size_y
        return x1, y1, x2, y2
    
    def _animate(self):
        self.win.redraw()
        time.sleep(.05)
        


