from random import randint, shuffle

def generate_test(count):
    names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]

    result = []

    for name in names:
        result = result + [name] * randint(1, count)
    
    shuffle(result)
    return result

def main():
    print(generate_test(5))

if __name__ == "__main__":
    main()
