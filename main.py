# This is a practice on Python.
import turtle
import math
t = turtle.Turtle()

def circle(length):
  for i in range(8):
    for c in ['red', 'green', 'yellow', 'blue', 'purple']:
      t.color(c)
      t.forward(length)
      t.left(45)
      t.forward(length)
      t.right(35)
      t.forward(length)

def center(): 
  t.pu()
  t.goto(-75, 170)
  t.pd()
  t.setheading(0)

def star(length):
  for i in ['red', 'green', 'yellow', 'blue', 'purple']:
    t.color(i)
    t.forward(length)
    t.right(144)

circle(20)
center()
star(100)