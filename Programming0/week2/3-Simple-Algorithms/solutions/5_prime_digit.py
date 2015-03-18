num = input("Enter n: ")
n = int(num)

def isPrime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True

result = False

while n > 0:
    if isPrime(n % 10):
        result = True
        break
    n = (n - (n % 10)) // 10

if result:
    print("yes")
else:
    print("no")
