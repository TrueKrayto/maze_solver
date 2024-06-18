from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def maze_params(W, H, S):
    rows = (H - S*2) // S
    cols = (W - S*2) // S
    return S, S, rows, cols, S, S


def main():
    width = 1200
    height = 800
    size = 50
    params = maze_params(width, height, size)
    win = Window(width, height)
    # maze args (x1, y1, rows, cols, cell size x, cell size y, window)
    maze = Maze(*params, win, seed=0)
    maze.create_cells()
    

    # wait for close starts the loop
    win.wait_for_close()

if __name__ == '__main__':
    main()

