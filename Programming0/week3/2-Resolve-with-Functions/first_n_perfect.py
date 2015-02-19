from is_perfect import is_perfect

def first_n_perfect(num):
    start = 1
    while num > 0:
        if is_perfect(start):
            num = num - 1
            print(start)
        start = start + 1
    
def main():
    n = input("Enter n: ")
    n = int(n)

    first_n_perfect(n)

if __name__ == "__main__":
    main()       
