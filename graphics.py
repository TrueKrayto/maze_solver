from tkinter import Tk, BOTH, Canvas, Button

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze runner")
        self.__root.resizable(False, False)
        self.__canvas = Canvas(self.__root, width=width, height=height, background="White")
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

    def draw_circle(self, circle):
        circle.draw_circle(self.__canvas)

    def butt_handler(self, text, func):
        self.solve_butt = Button(self.__root, text=text, command=func)
        self.solve_butt.pack() 

    def key_binder(self, key, func):
        self.__root.bind(key, func)

    def delete_obj(self, obj):
        self.__canvas.delete(obj)

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, point1, point2, width= 2):
        self.p1 = point1
        self.p2 = point2
        self.width = width

    def draw(self, canvas, color="black"):       
        canvas.create_line( self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=self.width)

    def __str__(self):
        return f"p1 = {self.p1.x},{self.p1.y} p2={self.p2.x},{self.p2.y}"

class Circle:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw_circle(self, canvas):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        canvas.create_oval(x1, y1, x2, y2, outline="blue", width=2, fill="lightblue", tags="sprite")

class Player:

    def __init__(self, win):
        self.win = win
        self.loc = (0,0)

    def draw_player(self, x, y, size):
        p1 = Point(x, y)
        self.loc = (p1.x, p1.y)
        p2 = Point(x + size, y + size)
        sprite = Circle(p1, p2)
        self.win.draw_circle(sprite)