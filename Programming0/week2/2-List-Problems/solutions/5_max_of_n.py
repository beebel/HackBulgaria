import sys

n = input("Enter n: ")
n = int(n)

count = 1
biggest = -sys.maxsize - 1

while count <= n:
    number = input()
    number = int(number)
    if number > biggest:
        biggest = number

    count += 1
    
print("Max is: " + str(biggest))
