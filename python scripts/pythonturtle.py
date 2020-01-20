from time import sleep
from random import randint
import turtle

bruh = turtle.Pen()
bruh.speed(0)
bruh.color("blue")

for side in range(randint(40,400)):
    bruh.forward(side)
    bruh.right(90)
