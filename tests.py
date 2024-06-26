import unittest
from maze import Maze
# tests wont work at the moment because maze does not work without a window currently
# need to move the if win==None condition in create cells
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )

if __name__ == "__main__":
    unittest.main()