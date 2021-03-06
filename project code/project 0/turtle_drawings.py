import turtle
import canvasvg

t = turtle.Turtle()
t.speed(0)
t.up()
t.goto((0,-300))
t.pencolor("maroon")
t.pensize(10)
t.circle(300)
for _ in range(90):                     # draw pieces of circle with dots around it
    t.down()
    t.circle(300, 4)
    t.up()
    t.right(90)
    t.fd(15)
    t.down()
    t.dot(8)
    t.up()
    t.back(15)
    t.left(90)
    
t.up()
t.goto((0,-275))                            # draw another solid circle
t.down()
t.fillcolor("maroon")
t.begin_fill()
t.circle(275)
t.end_fill()
t.pencolor("WhiteSmoke")                    # draw 3 lines of shrinking sizes
t.up()
t.goto((0,-250))
t.pensize(8)
t.down()
t.circle(250)
t.up()
t.goto((0,-225))
t.pensize(6)
t.down()
t.circle(225)
t.up()
t.goto((0,-200))
t.pensize(4)
t.down()
t.circle(200)

t.pensize(8)
t.up()
t.goto((-64, -100))
t.left(90)
t.down()
for _ in range(20):                             # draw the first line of the M
    t.left(90)                                  # with dots around it 
    t.up()
    t.fd(10)
    t.down()
    t.dot(8)
    t.up()
    t.back(10)
    t.down()
    t.right(90)
    t.fd(10)
t.up()                                          # work on the center 2 lines of the M
t.left(90)
t.fd(10)
t.down()
t.dot(8)
t.up()
t.back(10)
t.down()
t.left(130)
t.fd(100)
t.left(100)
t.fd(100)
t.right(140)

for _ in range(20):                             # do the other line of the M with the dots around it
    t.left(90)
    t.up()
    t.fd(10)
    t.down()
    t.dot(8)
    t.up()
    t.back(10)
    t.down()
    t.right(90)
    t.fd(10)
t.up()
t.left(90)
t.fd(10)
t.down()
t.dot(8)
t.up()
t.back(10)
t.down()
t.ht()

canvasvg.saveall('turtle.svg', t.getscreen().getcanvas()) # save as an svg
