from turtle import *
import turtle
import time
import math

shape('turtle')

speed(100)

def semicircle():
	for x in range(180):
		forward(1)
		left(1)

right(270)

semicircle()

right(180)

semicircle()

left(45)

forward(163.5)

left(90)

forward(163.5)

penup()

forward(100)

time.sleep(60)

