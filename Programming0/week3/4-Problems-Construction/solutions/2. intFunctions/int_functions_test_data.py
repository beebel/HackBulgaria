from random import randint

def randInt(maxInt):
    result = randint(1, maxInt)
    return result

def main():
    print(randInt(1000))

if __name__ == "__main__":
    main()
