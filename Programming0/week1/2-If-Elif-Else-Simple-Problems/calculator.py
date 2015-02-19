a = input ("Enter a:  ")
a = int(a)

b = input ("Enter b:  ")
b = int(b)

oper = input("Enter operation:  ")

print ("Result is:")

if (oper == '+'):
    print(a + b)
elif (oper == '-'):
    print(a - b)
elif (oper == '*'):
    print(a * b)
elif (oper == '/'):
    print(a / b)
else:
    print("We do not support that operation.")
    
