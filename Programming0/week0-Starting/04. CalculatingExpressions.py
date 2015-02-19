print (2 + 123)
print (2 * 2 + 213)
print (10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
print (1 + 1 + 2 + 3 + 5 + 8 + 13)
print (((13.0 / 8) + (8.0 / 5) + (5.0 / 3) + (3.0 / 2)) / 4)
print ("Python" * 2) # какъв е резултата? Как действа оператора *, когато има ляв операнд текст, и десен операнд число?
print (7 / 2) # real division, same as 7.0 / 2 or 7 / 2.0
print (7 / 2.0)
print (7 // 2) #integer division
print (7%2) # reminder

# Каква е разликата между операторите / и //?

# В Python REPL по ваш избор (IDLE / Python Command Line), напишете израз,
# който да отговаря на следните неща:

num1 = 1234
num2 = 5678

print (num1 + num2)

num1 = 88
num2 = 99

print (num1 * num2)

num1 = (pow(2, 32))
print ("here")
print (num1)
print (pow((num1)/2, 16))
print (pow(2, 16))

print ("omg" + "wtf")
print ("Spam" + " and" + "eggs")

num1 = 1
num2 = 6
sumDevident = 1
sumDivisor = 1

# Резултатът от умножението на числата от 1 до 10,
# разделени върху умножението на числата 6, 7, 8, 9 и 10.

while(num1<=10):
    sumDevident = num1 * sumDevident
    if(num1 == num2):
        sumDivisor = num2 * sumDivisor
        num2 = num2 + 1
    num1 = num1 + 1

result = sumDevident // sumDivisor
print (result)

# Колко са 20% от 100?

print ((20 * 100)/100)

# Колко са 35% от 1235?

print ((35 * 1235)/100)


