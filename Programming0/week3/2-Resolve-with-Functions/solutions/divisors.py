def divisors(num):
    i = 1
    divisorsList = []
    while i < num:
        if num % i == 0:
            divisorsList.append(i)
        i = i + 1
    return divisorsList

def main():
    n = input("Enter n: ")
    n = int(n)

    print(divisors(n))
            
    
if __name__ == "__main__":
    main()
