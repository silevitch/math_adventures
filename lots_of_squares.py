from turtle import *
import turtle
import time
import math

shape('turtle')
speed(100)

def square(length):
	for i in range(6):
		forward(length)
		right(90)

for x in range(100):
	square(x*5)
	right(x)

time.sleep(5)

ts = turtle.getscreen()

ts.getcanvas().postscript(file="lots_of_squares.eps")
