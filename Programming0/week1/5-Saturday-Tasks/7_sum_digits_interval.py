text = input("Enter N: ")
N = int(text)
text = input("Enter M: ")
M = int(text)

def sumPosN(num):
    sumPosN = 0
    while num > 0:
        lastPos = num % 10
        sumPosN = sumPosN + lastPos
        num = (num - lastPos) // 10

    return sumPosN            

while N <= M:
    print("Sum of digits of " + str(N) + " = " + str(sumPosN(N)))
    N = N + 1
