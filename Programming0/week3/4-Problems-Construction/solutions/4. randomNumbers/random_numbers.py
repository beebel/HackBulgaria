from random import randint

def generate_test(n, start, end):
    result = [randint(start, end) for n in range(n)]

    return result

def main():
    print(generate_test(5, 1, 3))

if __name__ == "__main__":
    main()
