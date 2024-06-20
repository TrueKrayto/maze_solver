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

    def butt_handler(self, text, func):
        self.solve_butt = Button(self.__root, text=text, command=func)
        self.solve_butt.pack() 

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

