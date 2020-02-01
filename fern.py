from turtle import *
import time
import math

shape('turtle')

speed(0)

for x in range(720):
	forward(x/8)
	right(4*x)

time.sleep(5)
