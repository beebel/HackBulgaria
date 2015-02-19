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
    if result[0] == "0":
        result = result[1:]

    return result

print(reverse(n))
