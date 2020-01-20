import turtle

bob = turtle.Pen()
bob.speed(0)
turtle.bgcolor("black")

numsides = turtle.numinput ("Number of sides", "How many sides do you want (1-8)", 4, 1, 8)
numsides = int(numsides)

colorlist = ["red", "blue", "purple", "orange", "yellow", "green", "aqua", "magenta"]

for number in range(300):
    bob.pencolor(colorlist[number%numsides])
    bob.forward(number)
    bob.left(360/numsides + 1) 
