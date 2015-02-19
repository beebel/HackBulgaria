num = input("Enter n: ")
n = int(num)

divisors = []

i = 1

while i < n:
    if n % i == 0:
        divisors.append(i)
    i += 1

print(divisors)    
