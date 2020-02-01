from turtle import *
import time
import math

shape('turtle')

def polygon(sides):
	for i in range(sides):
		forward(100)
		left(360/sides)

for x in range(8):
	polygon(x+3)

time.sleep(5)
