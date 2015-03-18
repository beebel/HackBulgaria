text = input("Enter number: ")
n = int(text)

sumPosN = 0

while (n > 0):
    lastPosN = n % 10
    sumPosN = sumPosN + lastPosN
    n = (n - lastPosN) // 10

print(sumPosN)    
