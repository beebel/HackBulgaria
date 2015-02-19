num = input("Enter n: ")
n = int(num)


def isPerfectNum(num):
    divisors = []

    i = 1
    sumDiv = 0

    while i < num:
        if num % i == 0:
            divisors.append(i)
        i += 1

    for e in divisors:
        sumDiv = sumDiv + e

    if sumDiv == num:
        return True
    else:
        return False


perfectNums = []
count = 1

while len(perfectNums) < n:

    if isPerfectNum(count):
        perfectNums.append(count)
    count = count + 1


for e in perfectNums:
    print (e)

