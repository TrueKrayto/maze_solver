from cell import Cell
from graphics import Window
import time, random
import sys

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.rows = num_rows
        self.cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.seed = seed
        if not self.seed:
            random.seed(self.seed)
        
      
    def create_cells(self):
        if self.win == None:
            return
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
                # self._animate()
        self._break_entrance_and_exit()
        sys.setrecursionlimit(100000)
        self._BREAK_WALLS_R(0,0)
        sys.setrecursionlimit(1000)
        for i in range(len(self.cells[0])):
            for j in range(len(self.cells)):
                pos = self._draw_cell(j, i)
                cell = self.cells[j][i]
                cell.draw(*pos)

    def _draw_cell(self, j, i):
        x1 = (j * self.cell_size_x) + self.x1
        x2 = x1 + self.cell_size_x
        y1 = (i * self.cell_size_y) + self.y1
        y2 = y1 + self.cell_size_y
        return x1, y1, x2, y2
    
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(.01)

    def _break_entrance_and_exit(self):
        first = self.cells[0][0]
        first.has_top_wall = False
        pos = self._draw_cell(0,0)
        first.draw(*pos)

        last = self.cells[self.cols-1][self.rows-1]
        last.has_bottom_wall = False
        pos = self._draw_cell(self.cols-1, self.rows-1)
        last.draw(*pos)

    def _BREAK_WALLS_R(self, col, row):
        # Mark the current cell as visited
        current = self.cells[col][row]
        current.visited = True
        
        # In an infinite loop:
        while True:
            # Create a new empty list to hold the i and j values you will need to visit
            to_visit = []
            #Check the cells adjacent to the current cell. Keep track of any not visited
            # check left
            if col > 0 and not self.cells[col-1][row].visited:
                to_visit.append((col-1, row))
            # check right
            if col < self.cols-1 and not self.cells[col+1][row].visited:
                to_visit.append((col+1, row))
            # check above
            if row > 0 and not self.cells[col][row-1].visited:
                to_visit.append((col, row-1))
            # check below
            if row < self.rows-1 and not self.cells[col][row+1].visited:
                to_visit.append((col, row+1))

            # If there are zero directions from current cell draw the current cell
            if len(to_visit) == 0:
                return
            # Otherwise, pick a random direction.
            else:
                next_pos = random.choice(to_visit)
                ncol, nrow = next_pos
                next_cell = self.cells[ncol][nrow] 
                # Knock down the walls between the current cell and the chosen cell.
                # left
                if ncol < col:
                    current.has_left_wall = False
                    next_cell.has_right_wall = False
                # up
                if nrow < row:
                    current.has_top_wall = False
                    next_cell.has_bottom_wall = False
                # right
                if ncol > col:
                    current.has_right_wall = False
                    next_cell.has_left_wall = False
                # down
                if nrow > row:
                    current.has_bottom_wall = False
                    next_cell.has_top_wall = False

               
                # Move to the chosen cell by recursively calling _break_walls_r
                self._BREAK_WALLS_R(ncol, nrow)
          

