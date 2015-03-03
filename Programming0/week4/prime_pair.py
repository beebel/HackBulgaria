from pairs import splitInput

def isPrime(n):
    result = True
    if n == 2:
        return result
    else:
        for i in range(2,n):
            if n % i == 0:
                result = False
                break    
        return result
    
def zero_neighbours_boolean(numbers):
    result = False
    if len(numbers) > 1:
        for i in range(len(numbers) - 1):
            if isPrime(numbers[i] + numbers[i + 1]):
                result = True
                break

    return result

def prime_pair(numbers):
    for num in numbers:
        if isPrime(num * 2):
            return True
        else:
            return zero_neighbours_boolean(numbers)
    
def main():
    txt = input("Enter your numbers here: ")

    print(prime_pair(splitInput(txt)))

if __name__ == "__main__":
    main()
