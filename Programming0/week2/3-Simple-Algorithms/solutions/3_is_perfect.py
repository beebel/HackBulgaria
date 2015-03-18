num = input("Enter n: ")
n = int(num)


divisors = []

i = 1
sumDiv = 0

while i < n:
    if n % i == 0:
        divisors.append(i)
    i += 1

for e in divisors:
    sumDiv = sumDiv + e

if sumDiv == n:
    print("is perfect")
else:
    print("is not perfect")
