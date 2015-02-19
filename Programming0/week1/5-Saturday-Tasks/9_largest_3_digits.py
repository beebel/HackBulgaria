text = input("Enter number: ")
n = int(text)

def posN(num):
    pos = []
    while (num > 0):
        lastPosN = num % 10
        pos.append(lastPosN)
        num = (num - lastPosN) // 10

    return pos

def bigger(a, b):
    if a >= b:
        return a
    else:
        return b    

def smaller(a, b):
    if a <= b:
        return a
    else:
        return b 
    
def biggestN(a, b, c):
    if max(a, b, c) == a:
        return a * 100 + bigger(b, c) * 10 + smaller(b, c)
    elif max(a, b, c) == b:
        return b * 100 + bigger(a, c) * 10 + smaller(a, c)
    else:
        return c * 100 + bigger(b, a) * 10 + smaller(b, a)
        
        
def smallestN(a, b, c):
    if min(a, b, c) == a:
        return a * 100 + smaller(b, c) * 10 + bigger(b, c)
    elif min(a, b, c) == b:
        return b * 100 + smaller(a, c) * 10 + bigger(a, c)
    else:
        return c * 100 + smaller(b, a) * 10 + smaller(b, a)
    
positions = posN(n)
n1 = positions[2]
n2 = positions[1]
n3 = positions[0]

print ("biggest number: " + str(biggestN(n1, n2, n3)))
print ("smallest number: " + str(smallestN(n1, n2, n3)))
