from time import sleep

x = 0
y = (x + 1)

for time in range(20):
    print(x)
    print(y)
    x = (x + y)
    y = (x + y)
    sleep(.5)
