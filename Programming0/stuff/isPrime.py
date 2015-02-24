def is_prime(x):
    result = False
    if x == 1 or x == 0:
        return result
    elif x == 2:
        return True
    else:
        i = 2
        while i < abs(x):
            if x % i == 0:
                break
            i  = i + 1
        else:
            result = True
    return result

def main():
    n = input("Enter n: ")
    n = int(n)
    print(is_prime(n))

if __name__ == "__main__":
    main()
