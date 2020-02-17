from turtle import *
import time
import math

shape('turtle')

length = 25 

def mountain(half_base):
	left(90)
	forward(length*half_base)
	right(90)
	for i in range((2*half_base)-1):
		if i % 2 == 0:
			right(45)
			forward(math.sqrt(length*length*2))
		else:
			left(45)
			forward(length)

	right(135)
	
	for i in range((2*half_base)-1):
		if i % 2 == 0:
			left(45)
			forward(math.sqrt(length*length*2))
		else:
			right(45)
			forward(length)


	right(135)
	forward(length*half_base)
	right(90)

left(90)
penup()
backward(length*14);
pendown()

for i in range(25):
	mountain(i+1)

time.sleep(5)
