"""
Lab1.py
Turtles!
"""
# Don't touch this also!
from turtle import *



def main():
    # Code underneath "defs" should be indented so the computer knows it's all part of the def
    # Thonny should automatically indent for you though, so no need to worry about it
    
    # Don't touch this code!
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.resizemode("auto")
    turtle.pensize(turtle.pensize() * 7)
    turtle.pencolor("navy blue")
    turtle.speed(25)
    
    # <- This pound sign tells the computer that everything on the rest of line is a comment
    # The computer ignores comments when you're program is running, so they can be used to give
    # important information
    
    # Thonny will also gray out comments to help you visualize what is commented and what is not

    # You can also comment out code! Right now this line is commented, so the computer will ignore it
    # However, you can remove the # in front to uncomment the line and the computer will then run that code
    # Try uncommenting the next line and see what happens when you run the code!
    # Try recommenting the code and see what is different when you run it!
    
    #turtle.forward(150)

    #turtle.backward(150)
    
    #turtle.right(90)
    #turtle.forward(150)
    
    #turtle.left(90)
    #turtle.forward(150)
    
    #turtle.circle(75)

    #turtle.circle(75, 180)

    #turtle.up()
    #turtle.forward(200)

    turtle.down()
    
    # we can make a square by doing this:
    
    #turtle.forward(100)
    #turtle.right(90)
    #turtle.forward(100)
    #turtle.right(90)
    #turtle.forward(100)
    #turtle.right(90)
    #turtle.forward(100)
    #turtle.right(90)
    
    # or we can use a loop like this!
    #for _ in range(4):

# DON'T GIVE THIS LINE
        #turtle.forward(100)
        #turtle.right(90)
        
    # use this template to make a equalaterial triangle
    # hint: each angle in an equalaterial triangle is 60 degrees,
    # so the inside angle must equal 60. if the inside = 60, we need to turn the turtle
    # what minus 60 degrees?
    #for _ in range():
        #turtle.forward()
        #turtle.left()
    
    # now try to make your own polygons! you can use this base template if you want!
    #for _ in range():
    
    
    # fancier loops:

# LOOP A
    #size = 146
    #for count in range(4):
    #  print("count: {}".format(count))
    #  turtle.forward(size)
    #  turtle.left(90)
    #  size = size - 5

# LOOP B
    #for count in range(360):
    #  print("count: {}".format(count))
    #    turtle.forward(count)
    #    turtle.left(59)

# LOOP C
    #for count in range(30):
    #  print("count: {}".format(count))
    #    turtle.circle(5*count)
    #    turtle.circle(-5*count)
    #    turtle.left(count)
    
        


# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()
