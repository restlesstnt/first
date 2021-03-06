# This is a practice on Python.
import turtle
import math
t = turtle.Turtle()
t.speed(100)

def circle(length):
  for i in range(8):
    for c in ['red', 'green', 'yellow', 'blue', 'purple']:
      t.color(c)
      t.forward(length)
      t.left(45)
      t.forward(length)
      t.right(35)
      t.forward(length)

def star(length):
  for i in ['red', 'green', 'yellow', 'blue', 'purple']:
    t.color(i)
    t.forward(length)
    t.right(144)

def small_diamond(): # diamond exterior
  t.setheading(45)
  t.forward(100)
  t.right(90)
  for i in range(3):
    t.forward(400)
    t.right(90)
  t.forward(400)
  t.home()

def diamond_row():
  t.setheading(-45) # set angle
  for i in range(4): # constructs 4 squares per row
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.back(100)
    t.right(90)
  t.back(400) # moves back and starts a new row 
  t.right(90)
  t.forward(100)
  t.left(90)
  for i in range(4):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.back(100)
    t.right(90)
  t.back(400)
  t.right(90)
  t.forward(100)
  t.left(90)
  for i in range(4):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.back(100)
    t.right(90)
  t.back(400)
  t.right(90)
  t.forward(100)
  t.left(90)
  for i in range(4):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.back(100)
    t.right(90)
  t.back(400) # back to original position 
  t.left(90)
  t.forward(400)
  t.setheading(-45)
  
def big_diamond():
  t.fillcolor(255,0,0) # red
  t.begin_fill()
  for i in range(3):
    t.forward(100)
    t.right(90)
  t.end_fill()
  t.fillcolor(255,165,0) # orange
  t.begin_fill()
  t.right(90)
  t.forward(200)
  t.left(90)
  for i in range(2):
    t.forward(100)
    t.left(90)
  t.forward(200)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.end_fill()
  t.fillcolor(255,255,0) # yellow
  t.back(100)
  t.right(90)
  t.begin_fill()
  for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
  t.forward(100)
  t.right(90)
  for i in range(3):
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
  t.end_fill()
  t.fillcolor(0,128,0) # green
  t.begin_fill()
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.right(90)
  t.forward(200)
  t.end_fill()
  t.back(200)
  t.fillcolor(0,0,255) # blue
  t.begin_fill()
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(200)
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.end_fill()
  t.right(180)
  t.fillcolor(75,0,130) # purple
  t.begin_fill()
  t.right(90)
  t.forward(100)
  t.left(90)
  t.forward(200)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(100)
  t.right(90)
  t.forward(200)
  t.end_fill()
  t.back(200)
  t.fillcolor(255,105,180) # pink
  t.begin_fill()
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.left(90)
  t.forward(100)
  t.end_fill()
  
# call to function
small_diamond()
diamond_row()
big_diamond()