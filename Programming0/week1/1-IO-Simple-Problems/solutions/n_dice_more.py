import random

var = input("Enter sides: ")
n = int(var)

dices = []
sumDices = 0

def roll():
    result = random.randint(1, n)
    dices.append(result)
    return result

print("First roll:")
print(roll())
print("Second roll:")
print(roll())

for e in dices:
    sumDices = sumDices + e

print("Sum is:")
print(sumDices)
    
    
