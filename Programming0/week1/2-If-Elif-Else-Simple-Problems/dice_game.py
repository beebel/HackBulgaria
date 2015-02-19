import random

n = input("Enter dice side:   ")
n = int(n)
name1 = input("Enter player1 name:  ")
name2 = input("Enter player2 name:  ")

plrDice1 = random.randint(1, n)
plrDice2 = random.randint(1, n)

print("%s rolls %d" %(name1, plrDice1))
print("%s rolls %d" %(name2, plrDice2))

if plrDice1 > plrDice2:
    print("%s wins!" %(name1))
elif plrDice1 < plrDice2:
    print("%s wins!" %(name2))
else:
    print("Draw!")



