from graphics import Line, Point

class Cell:

    def __init__(self, win):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True        
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win =  win
        self.visited = False
        self.goal = False
        
    def center_finder(self):
        if self._x1:
            if self._x2:
                if self._y1:
                    if self._y2:
                        return ((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)
        return None
                
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:            
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "White")

        if self.has_top_wall:            
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")

        if self.has_right_wall:            
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")

        if self.has_bottom_wall:            
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo= False):
        start = self.center_finder()        
        finish = to_cell.center_finder()
        if start and finish:
            start_point = Point(start[0], start[1])
            finish_point = Point(finish[0], finish[1])
            path = Line(start_point, finish_point, 4)
            if undo:
                self._win.draw_line(path, "gray")
            else:
                self._win.draw_line(path, "red")



