a = input("Enter a:  ")
a = int(a)
b= input("Enter b:  ")
b = int(b)

def printNumAtoB (lower, upper):
    while (lower <= upper):
        print (lower)
        lower = lower + 1

if(a > b):
    printNumAtoB (b, a)
elif (a < b):
    printNumAtoB (a, b)
else:
    print (a)

    
