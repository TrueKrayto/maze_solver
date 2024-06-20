from cell import Cell
from tkinter import Button
from graphics import Player
import time, random
import sys

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        # Initialize the maze with given parameters
        self.x1 = x1
        self.y1 = y1
        self.rows = num_rows
        self.cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.player = None
        self.seed = seed
        if not self.seed:
            random.seed(self.seed)
        if self.win:
            self.playr_start() 
            self.win.butt_handler("solve", self.solve)
            self.win.key_binder('<space>',self.solve_key)
            self.win.key_binder('<Down>',self.move_player_down)
            self.win.key_binder('<Up>',self.move_player_up)
            self.win.key_binder('<Right>',self.move_player_right)
            self.win.key_binder('<Left>',self.move_player_left)
          

    def test(self, event):
        self.win.delete_obj("sprite")   

    def playr_start(self):
        sprite = Player(self.win)
        self.player = sprite
        sprite.draw_player(self.cell_size_x, self.cell_size_y, self.cell_size_x)   
        

    def create_cells(self):
        # Create cell objects for the maze
        if not self.win:
            return
        all_cells = []
        for col in range(self.cols):
            column = []
            for row in range(self.rows):
                cell = Cell(self.win)
                column.append(cell)
            all_cells.append(column)
        self.cells = all_cells

        # Set the goal cell
        self.cells[self.cols-1][self.rows-1].goal = True

        # Draw all cells
        for i in range(self.rows):
            for j in range(self.cols):
                pos = self._draw_cell(j, i)
                cell = self.cells[j][i]
                cell.draw(*pos)
                self._animate()

        self._break_entrance_and_exit()
        
        # Increase recursion limit for larger mazes
        sys.setrecursionlimit(100000)
        self._BREAK_WALLS_R(0, 0)
        self._reset_visited()
        sys.setrecursionlimit(1000)
        
        # Redraw all cells after breaking walls
        for i in range(self.rows):
            for j in range(self.cols):
                pos = self._draw_cell(j, i)
                cell = self.cells[j][i]
                cell.draw(*pos)
                self._animate()

    def _draw_cell(self, j, i):
        # Calculate the coordinates for drawing a cell
        x1 = (j * self.cell_size_x) + self.x1
        x2 = x1 + self.cell_size_x
        y1 = (i * self.cell_size_y) + self.y1
        y2 = y1 + self.cell_size_y
        return x1, y1, x2, y2

    def _animate(self):
        # Redraw the window with a slight delay for animation effect
        if not self.win:
            return
        self.win.redraw()
        time.sleep(.001)

    def _break_entrance_and_exit(self):
        # Break walls for entrance and exit
        first = self.cells[0][0]
        first.has_top_wall = False
        pos = self._draw_cell(0, 0)
        first.draw(*pos)

        last = self.cells[self.cols-1][self.rows-1]
        last.has_bottom_wall = False
        pos = self._draw_cell(self.cols-1, self.rows-1)
        last.draw(*pos)

    def _BREAK_WALLS_R(self, col, row):
        # Recursive function to break walls and create a maze
        current = self.cells[col][row]
        current.visited = True

        while True:
            to_visit = []
            if col > 0 and not self.cells[col-1][row].visited:
                to_visit.append((col-1, row))
            if col < self.cols-1 and not self.cells[col+1][row].visited:
                to_visit.append((col+1, row))
            if row > 0 and not self.cells[col][row-1].visited:
                to_visit.append((col, row-1))
            if row < self.rows-1 and not self.cells[col][row+1].visited:
                to_visit.append((col, row+1))

            if len(to_visit) == 0:
                return
            else:
                ncol, nrow = random.choice(to_visit)
                next_cell = self.cells[ncol][nrow]

                if ncol < col:
                    current.has_left_wall = False
                    next_cell.has_right_wall = False
                if nrow < row:
                    current.has_top_wall = False
                    next_cell.has_bottom_wall = False
                if ncol > col:
                    current.has_right_wall = False
                    next_cell.has_left_wall = False
                if nrow > row:
                    current.has_bottom_wall = False
                    next_cell.has_top_wall = False

                self._BREAK_WALLS_R(ncol, nrow)

    def _reset_visited(self):
        # Reset the visited status for all cells
        for i in range(self.cols):
            for j in range(self.rows):
                self.cells[i][j].visited = False

    def solve_key(self, event):
        self.solve()

    def solve(self):
        # Solve the maze starting from the top-left corner
        return self._solve_r(0, 0)

    def _solve_r(self, col, row):
        # Recursive function to solve the maze
        sys.setrecursionlimit(100000)
        self._animate()
        current = self.cells[col][row]
        current.visited = True

        if current.goal:
            return True

        directions = []
        if not current.has_left_wall and col > 0 and not self.cells[col-1][row].visited:
            directions.append((col-1, row))
        if not current.has_top_wall and row > 0 and not self.cells[col][row-1].visited:
            directions.append((col, row-1))
        if not current.has_right_wall and col < self.cols-1 and not self.cells[col+1][row].visited:
            directions.append((col+1, row))
        if not current.has_bottom_wall and row < self.rows-1 and not self.cells[col][row+1].visited:
            directions.append((col, row+1))

        random.shuffle(directions)

        for ncol, nrow in directions:
            next_cell = self.cells[ncol][nrow]
            current.draw_move(next_cell)
            if self._solve_r(ncol, nrow):
                return True
            else:
                current.draw_move(next_cell, undo=True)

        return False
    
    def move_player_down(self, event):
        location = self.player.loc
        col = (location[0] // self.cell_size_x) - 1
        row = (location[1] // self.cell_size_y) - 1
        cell = self.cells[col][row]
        if not cell.has_bottom_wall:
            self.win.delete_obj("sprite")
            self.player.draw_player(location[0], location[1] + self.cell_size_y, self.cell_size_x)

    def move_player_up(self, event):
        location = self.player.loc
        col = (location[0] // self.cell_size_x) - 1
        row = (location[1] // self.cell_size_y) - 1
        cell = self.cells[col][row]
        if not cell.has_top_wall and row!= 0:
            self.win.delete_obj("sprite")
            self.player.draw_player(location[0], location[1] - self.cell_size_y, self.cell_size_x)

    def move_player_right(self, event):
        location = self.player.loc
        col = (location[0] // self.cell_size_x) - 1
        row = (location[1] // self.cell_size_y) - 1
        cell = self.cells[col][row]
        if not cell.has_right_wall:
            self.win.delete_obj("sprite")
            self.player.draw_player(location[0]  + self.cell_size_x, location[1], self.cell_size_x)

    def move_player_left(self, event):
        location = self.player.loc
        col = (location[0] // self.cell_size_x) - 1
        row = (location[1] // self.cell_size_y) - 1
        cell = self.cells[col][row]
        if not cell.has_left_wall:
            self.win.delete_obj("sprite")
            self.player.draw_player(location[0]  - self.cell_size_x, location[1], self.cell_size_x)