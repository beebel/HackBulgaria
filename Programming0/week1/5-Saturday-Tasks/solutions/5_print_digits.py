text = input("Enter number: ")
n = int(text)

while (n > 0):
    lastPosN = n % 10 
    print(lastPosN)
    n = (n - lastPosN) // 10
