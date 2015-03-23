import random

def generate_test():
    oddNums = [x for x in range(1, 20) if x % 2 == 1]
    num = random.choice(oddNums)

    return num

def main():
    print(generate_test())

if __name__ == "__main__":
    main()
