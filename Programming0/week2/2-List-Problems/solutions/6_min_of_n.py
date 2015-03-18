import sys

n = input("Enter n: ")
n = int(n)

count = 1
smallest = sys.maxsize

while count <= n:
    number = input()
    number = int(number)
    if number < smallest:
        smallest = number

    count += 1
    
print("Max is: " + str(smallest))
