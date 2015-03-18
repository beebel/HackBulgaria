text = input("Enter number: ")
n = int(text)

def posN(num):
    pos = []
    while (num > 0):
        lastPosN = num % 10
        pos.append(lastPosN)
        num = (num - lastPosN) // 10

    return pos

def reverse(a):
    result = ""
    list = posN(a)
    for e in list:
        result = result + str(e)

    return result

if reverse(n) == str(n):
    print("The number is palindrom")
else:
    print("The number is not palindrom")
