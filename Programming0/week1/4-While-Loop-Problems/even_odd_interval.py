a = input("Enter a:  ")
a = int(a)
b= input("Enter b:  ")
b = int(b)

def printNumAtoB (lower, upper):
    while (lower <= upper):
        print ("%d - %s" %(lower, oddOrEven(lower)))
        lower = lower + 1

def oddOrEven (num):
    if (num % 2 == 0):
        return "even"
    else:
        return "odd"

if(a > b):
    printNumAtoB (b, a)
elif (a < b):
    printNumAtoB (a, b)
else:
    print ("%d - %s" % (a, oddOrEven(a)))
    
