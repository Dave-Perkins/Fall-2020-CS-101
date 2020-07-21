from turtle import *
import random


class Turtle_Drawings():
    
    
    def __init__(self, shape, size, speed):
        self._turtle = Turtle()
        self._turtle.shape('turtle')
        colormode(255)
        self._turtle.resizemode('auto')
        self._turtle.pensize(size)
        self._turtle.speed(speed)
        
        self._pensize = size
        self._speed = speed
        self._shape = shape
                
    def get_speed(self):
        return self._speed
    
    def set_speed(self, newspeed):
        self._speed = newspeed
        self._turtle.speed(newspeed)
    
    def get_pensize(self):
        return self._pensize
    
    def set_pensize(self, newsize):
        self._pensize = newsize
        self._turtle.pensize(newsize)
        
    def get_shape(self):
        return self._shape
    
    def set_shape(self, newshape):
        self._shape = newshape
        
        
    def draw_triangle(self, length):
        for _ in range(3):
            self._turtle.forward(length)
            self._turtle.left(120)
        
    def draw_square(self, length):
        for _ in range(4):
            self._turtle.forward(length)
            self._turtle.left(90)
            
    def draw_pentagon(self, length):
        for _ in range(5):
            self._turtle.forward(length)
            self._turtle.left(72)
        
    def draw_spirograph(self, x, y, width):
        self._turtle.up()
        self._turtle.goto(x, y)
        self._turtle.down()
        
        
        for num_petals in range(36):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self._turtle.pencolor(r, g, b)
            
            if self._shape.upper() == "SQUARE":
                self.draw_square(width)
            elif self._shape.upper() == "CIRCLE":
                self._turtle.circle(width)
            elif self._shape.upper() == "TRIANGLE":
                self.draw_triangle(width)
            elif self._shape.upper() == "PENTAGON":
                self.draw_pentagon(width)
            else:
                print("Unrecognized Shape!")


            self._turtle.up()
            self._turtle.goto(x, y)
            self._turtle.down()
            self._turtle.left(10)
              
        
    def draw_recursion(self, x, y, length):
        if length < 1:
            return
        
        self._turtle.up()
        self._turtle.goto(x, y)
        self._turtle.down()
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self._turtle.pencolor(r, g, b)
        
        if self._shape.upper() == 'CIRCLE':
            self._turtle.circle(length)
        elif self._shape.upper() == 'TRIANGLE':
            self.draw_triangle(length)
        elif self._shape.upper() == 'SQUARE':
            self.draw_square(length)
        elif self._shape.upper() == 'PENTAGON':
            self.draw_pentagon(length)
        else:
            print("Shape not recognized")
        
        x_mod = 15
        y_mod = x_mod
        length_mod = -(x_mod * 2)
        self.draw_recursion(x + x_mod, y + y_mod, length + length_mod)
        


def main():
    drawings = Turtle_Drawings("square", 5, 0)
    #drawings.draw_spirograph(0, 0, 150)
    #drawings.draw_recursion(0, 0, 530)
    #drawings.draw_triangle(100)

if __name__ == "__main__":
    main()