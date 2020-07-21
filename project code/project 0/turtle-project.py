"""
CS101 Project 0 Example
Gwen Urbanczyk
"""
from turtle import *

def draw_spiral(turtle):
    """
    Function draws hexagonal spiral rainbow pattern
    """
    colors = ["red", "purple", "blue", "green", "orange", "yellow"]
    
    for count in range(360):
        color = colors[count % 6]
        turtle.pencolor(color)
        
        turtle.width(count // 50 + 1)
        turtle.forward(count)
        turtle.left(59)

def draw_house(turtle):
    """
    Function draws a nice house, some clouds, and the sun
    """
    
    screen = turtle.getscreen()
    screen.bgcolor("sky blue")
    
    turtle.up()
    turtle.goto(-475, -300)
    turtle.down()
    turtle.pencolor("green")
    turtle.fillcolor("green")
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.forward(1150)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
        
    turtle.end_fill()
    
    turtle.pencolor("midnight blue")
    
    turtle.up()
    turtle.goto(300,-300)
    turtle.down()
     
    turtle.fillcolor("beige")
    turtle.begin_fill()
     
    for _ in range(4):
        turtle.left(90)
        turtle.forward(300)
        
        
    turtle.end_fill()
    
    
    turtle.backward(200)
    turtle.left(180)
    
    turtle.fillcolor("red")
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.right(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        
    turtle.end_fill()
        
    turtle.right(180)
    turtle.forward(80)
    turtle.up()
    turtle.left(90)
    turtle.forward(60)
    turtle.down()
    turtle.fillcolor("midnight blue")
    turtle.begin_fill()
    turtle.circle(6)
    turtle.end_fill()
    
    turtle.up()
    turtle.goto(0,0)
    
    turtle.backward(125)
    turtle.right(90)
    turtle.forward(25)
    turtle.down()
    
    turtle.fillcolor("white")
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.forward(75)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        
    turtle.end_fill()
    
    turtle.forward(37.5)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(37.5)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(75)
    
    turtle.up()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(175)
    turtle.down()
    
    turtle.fillcolor("white")
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.forward(75)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        
    turtle.end_fill()
    
    turtle.forward(37.5)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(37.5)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(75)
    
    turtle.up()
    turtle.goto(0,0)
    turtle.down()
    
    turtle.fillcolor("grey")
    turtle.begin_fill()

    for _ in range(2):
        turtle.right(120)
        turtle.forward(300)
        
    turtle.end_fill()
        
    turtle.pencolor("yellow")
    turtle.fillcolor("yellow")
    turtle.up()
    turtle.goto(350,250)
    
    turtle.down()
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
        
    turtle.up()
    turtle.goto(-100, 200)
    turtle.down()
    
    turtle.pencolor("snow2")
    turtle.fillcolor("snow2")
    
    turtle.right(120)
    
    for _ in range(4):
        turtle.begin_fill()
        turtle.circle(75)
        turtle.end_fill()
        turtle.up()
        turtle.forward(90)
        turtle.down()
        
    turtle.up()
    turtle.goto(-150, 275)
    turtle.down()
    
    for _ in range(3):
        turtle.begin_fill()
        turtle.circle(75)
        turtle.end_fill()
        turtle.up()
        turtle.forward(90)
        turtle.down()


def main():
    """
    Program draws some stuff using turtles! I included both project examples
    of the house and the spiral pattern.
    One is much more mechanically complicated (spiral),
    but is much less code,
    while the house is a lot of code, but none of it is too complicated.
    Also in reality, they would not be functions, but I put them in
    to make this code more readable/usable.
    """
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.resizemode("auto")
    turtle.pensize(turtle.pensize() * 7)
    turtle.pencolor("navy blue")
    #turtle.speed(0)
    
    draw_house(turtle)
    
    # Or
    
    #draw_spiral(turtle)
        


# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()
