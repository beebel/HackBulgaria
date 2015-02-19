text = input("Enter number: ")
n = int(text)

result = True
i = 2

while i < n:
    if n % i == 0:
        result = False
        break
    i = i + 1

if result == True:
    print("The number is prime!")
else:
    print("The number is not prime!")
