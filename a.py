from math import *
from turtle import *
from time import sleep
from random import randint
import keyboard



def setup():
	bgcolor('black')
	color('black')
	speed(0)
	return

def colors():
	a = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
	string = '#'
	for i in range(6):
		string += str(a[randint(0,9)])
	return string

def draw( R,k,k2,p,h ):
	write("k:"+str(k)+", k2: "+str(k2)+", p: "+str(p)+", h:"+str(h))
	r = R/k
	r2 = R/k2
	x = (R + r) * cos(0) + (r + r2) * cos(0 + (R*0)/r - R*0/(p*r)) + h * cos(0 + R*0/r - R*0/(p*r) - R*0/(p*r2))
	y = (R + r) * sin(0) + (r + r2) * sin(0 + (R*0)/r - R*0/(p*r)) + h * sin(0 + R*0/r - R*0/(p*r) - R*0/(p*r2))
	t = 0
	start = [x,y]
	goto(x,y)
	color('red')
	while(True):
		if keyboard.is_pressed('q'):
			break
		oldx = x
		oldy = y
		goto(oldx,oldy)
		x = (R + r) * cos(t) + (r + r2) * cos(t + (R*t)/r - R*t/(p*r)) + h * cos(t + R*t/r - R*t/(p*r) - R*t/(p*r2))
		y = (R + r) * sin(t) + (r + r2) * sin(t + (R*t)/r - R*t/(p*r)) + h * sin(t + R*t/r - R*t/(p*r) - R*t/(p*r2))
		t += 0.1
	done()
	return


R = 80
k = 3/2
k2 = 3.98
p = 0.5
h = 100

setup()
draw(R,k,k2,p,h)
