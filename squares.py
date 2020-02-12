from turtle import *
import turtle
import time
import math

shape('turtle')

def square():
	for i in range(4):
		forward(100)
		right(90)

for x in range(60):
	square()
	right(5)

time.sleep(5)

ts = turtle.getscreen()

ts.getcanvas().postscript(file="squares.eps")
