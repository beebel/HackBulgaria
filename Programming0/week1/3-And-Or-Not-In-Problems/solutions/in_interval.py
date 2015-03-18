a = input ("Enter a: ")
a = int(a)
b = input ("Enter b: ")
b = int(b)
x = input ("Enter x: ")
x = int(x)

if (x == a):
    print("The number is equal to the lower bound of the interval")
elif (x == b):
    print("The number is equal to the upper bound of the interval")
elif ((x > a) and (x < b)):
    print("The number is in the interval")
elif (x < a):
    print("The number is outside the interval, x < a")
else:
    print("The number is outside the interval, x > b")

