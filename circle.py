from turtle import *
import time
import math

shape('turtle')

speed(100)

for x in range(360):
	forward(x)
	right(x)

time.sleep(5)
