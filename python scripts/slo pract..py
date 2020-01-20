import random

integerList = []
total = 0

for numlist in range(5):
    randInt = random.randint(1, 100)
    integerList.append(randInt)
    total = total + randInt

mean = total/len(integerList)

print(mean)

if mean > 50:
    print("The mean is greater than 50.")
if mean < 50:
    print("The mean is less than 50.")
if mean == 50:
    print("The mean is 50.")

def function(): 
    print("bruhmoment")

function()
