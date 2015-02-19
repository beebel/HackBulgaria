from divisors import divisors

def sum_ints(numbers):
    sumNum = 0
    for e in numbers:
        sumNum = sumNum + e
    return sumNum

def main():
    n = input("Enter n: ")
    n = int(n)

    print(divisors(n))
    print(sum_ints(divisors(n)))
            
    
if __name__ == "__main__":
    main()

