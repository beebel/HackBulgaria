from sum_divisors import sum_ints
from divisors import divisors

def is_perfect(num):
    result = False
    if sum_ints(divisors(num)) == num:
        result = True
        return result
    else:
        return result

def main():
    n = input("Enter n: ")
    n = int(n)

    print(divisors(n))
    print(sum_ints(divisors(n)))
    print("Is %d a perfect number?" % n)
    print(is_perfect(n))
            
    
if __name__ == "__main__":
    main()    
