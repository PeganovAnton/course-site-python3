#!/bin/env python3

from record import start, finish
import turtle
import math

r = 100
n = 50
a = 2*r*math.sin(math.pi/n)
b = 180*(1-2/n)

start(2*r, 2*r, 0, 0, 50, __file__)

turtle.penup()
turtle.forward(r)
turtle.left(180-b/2)
turtle.pendown()

for i in range(n):
    turtle.forward(a)
    turtle.left(180-b)

finish()