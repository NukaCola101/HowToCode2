# Fashion Pattern - Python Code - Elizabeth Tweedale

from turtle import *                # import the turtle module
from random import randint          # import randint from the random module

designer = Turtle()                 # declare your Turtle as designer
designer.penup()                    # lift up the pen in order to move it to the correct place
designer.hideturtle()               # hide the turtle drawing arrow
designer.goto(-330,330)             # send the designer to the top left corner

r, g, b = 0, 0, 0                   # creaet 3 numbers r, g, b to create colors
colormode(255)                      # set the color mode to 255
                                    # speed(0)

def chooseColor():                  # this function will choose a random color
    global r,g,b                
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
   
    designer.pencolor(r,g,b)        # set the pen color to the random color
    designer.fillcolor(r,g,b)       # set the fill color to the random color
    
    #print ("Color is:", r, g, b)    # you don't need this line of code, you can just use it for testing
                                    # it will print the color to the IDLE window for you to see

def drawSquare(size):               # this function will draw a square
    designer.begin_fill()           # create a filled square
    designer.pendown()              # set the pen down
    for i in range(4):              # draw the square
        designer.forward(size)      # this will be the size of the square - try changing the number to change the size
        designer.right(90)
    designer.penup()                # set the pen up so that you can move the designer
    designer.end_fill()

    #print ("Square Drawn")          # this is also not needed, just used for testing

def drawOneRow(number, size):         # this function will draw a row of squares
    for i in range(number):           # draw 10 squares - you can change this number to make more or less!
        chooseColor()               # call the chooseColor() function to change the color each time you draw a square
        drawSquare(size)            # draw a filled square
        designer.forward(size+20)      # move forward before drawing the next square
                                    # HINT: make sure this number is the same as the move forward amount in drawSquare()
                                    #       you can test out different numbers to change the spacing

def drawPattern(number, size):      # this function will draw the final pattern
    for j in range(number):             
        drawOneRow(number, size)        # now, draw ten rows and move down after each one
        designer.backward((size+20)*number)  # we now work out how far back to move
        designer.right(90)
        designer.forward(size+20)
        designer.left(90)

drawPattern(10, 25)                 # call the function to draw your pattern
                                    # - > the first number is the number of squares
                                    # - > the second number is the size of the squares
