text = input("Enter number: ")
n = int(text)

i = 1
sumEven = 0

while i <= n:
    if i % 2 == 0:
        sumEven = sumEven + i
    i = i + 1

print(sumEven)     
