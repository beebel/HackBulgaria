num = input("Enter p: ")
p = int(num)

def isPrime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i = i + 1
    return True

if isPrime(p):
    if isPrime(p - 2) or isPrime(p + 2):
        print("Twin primes with " + str(p) + ":")
        if isPrime(p - 2):
            print(str(p - 2) + ", " + str(p))
        if isPrime(p + 2):
            print(str(p) + ", " + str(p + 2))
    else:
        print(str(p) + " is prime but:")
        print(str(p - 2) + " is not")
        print(str(p + 2) + " is not")

else:
    print(str(p) + " is not a prime")
