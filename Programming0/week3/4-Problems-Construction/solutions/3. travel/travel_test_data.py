from random import randint

def generate_test(maxLines):
    result = [randint(1, 60) for n in range(randint(1, maxLines))]

    return result

def main():
    print(generate_test(5))

if __name__ == "__main__":
    main()
