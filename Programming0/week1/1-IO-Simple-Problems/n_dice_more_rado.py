from random import randint

n = input("Enter sides: ")
# Превръщаме string-a в int. Всеки input е string
n = int(n)

dice_roll_1 = randint(1, n)
dice_roll_2 = randint(1, n)
sum = dice_roll_1 + dice_roll_2

print("First roll:")
print(dice_roll_1)
print("Second roll:")
print(dice_roll_2)
print("Sum is:")
print(sum)
