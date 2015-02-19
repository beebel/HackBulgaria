text = input("Enter number: ")
n = int(text)

i = 1
sumOdd = 0

while i <= n:
    if i % 2 == 1:
        sumOdd = sumOdd + i
    i = i + 1

print(sumOdd)   
