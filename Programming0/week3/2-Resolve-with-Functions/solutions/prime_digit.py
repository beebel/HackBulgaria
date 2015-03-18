def is_prime(num):
    i = 2
    result = True
    if num == i:
        return result
    while i < num:
        if num % i == 0:
            result = False
            break
        else:
            i = i + 1

    return result

def to_digits(number):
    nums = []
    i = 0
    while i < len(number):
        nums.append(int(number[i]))
        i = i + 1        

    return nums    

def isAtLeast1PrimeDigitInN(numList):
    result = False
    for e in to_digits(numList):
        if is_prime(e):
            result = True
            break

    return result

def main():
    n = input("Enter : ")

    print(isAtLeast1PrimeDigitInN(to_digits(n)))
        

    
if __name__ == "__main__":
    main()
