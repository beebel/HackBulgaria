n = input("Enter n: ")
n = int(n)


def isEven(n):
    if n % 2 == 0 and n != 0:
        return True
    else:
        return False

evenNum = []
count = 1

while count <= n:
    number = input()
    number = int(number)

    if isEven(number):
        evenNum.append(number)

    count += 1

print("Count of evens: " + str(len(evenNum)))
print("Evens are:")

for e in evenNum:
    print (e)
    
