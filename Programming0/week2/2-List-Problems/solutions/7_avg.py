n = input("Enter n: ")
n = int(n)

count = 1
sumNum = 0

while count <= n:
    number = input()
    number = int(number)

    sumNum = sumNum + number

    count += 1

print(sumNum / n)
