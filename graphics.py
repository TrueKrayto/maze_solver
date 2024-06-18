from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze runner")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, color="black"):
        line.draw(self.__canvas, color)

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, color="black"):       
        canvas.create_line( self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=2)

    def __str__(self):
        return f"p1 = {self.p1.x},{self.p1.y} p2={self.p2.x},{self.p2.y}"

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
        if self.has_top_wall:            
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:            
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:            
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo= False):
        start = self.center_finder()        
        finish = to_cell.center_finder()
        if start and finish:
            start_point = Point(start[0], start[1])
            finish_point = Point(finish[0], finish[1])
            path = Line(start_point, finish_point)
            if undo:
                self._win.draw_line(path, "gray")
            else:
                self._win.draw_line(path, "red")

