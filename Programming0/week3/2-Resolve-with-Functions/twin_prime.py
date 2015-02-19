from prime_digit import is_prime

def main():
    n = input("Enter n: ")
    n = int(n)

    if is_prime(n):
        if is_prime(n - 2) or is_prime(n + 2):
            print("Twin primes with %d:" %n)
            if is_prime(n - 2):
                print("%d %d" %(n - 2, n))
            if is_prime(n + 2):
                print("%d %d" %(n, n + 2))
        else:
            print("%d is prime but:" %n)
            print("%d is not" % (n - 2))
            print("%d is not" % (n + 2))
    else:
        print("%d is not a prime" %n)
        

    
if __name__ == "__main__":
    main()
