import random

def generate_test(maxSidesSquare):
    result = []
    numbers = [i for i in range(1, 51)]
    sides = random.randint(2,maxSidesSquare)
    for line in range(1, sides + 1):
        result.append([random.choice(numbers) for n in range(sides)])

    return result

def print_square(squareLst):
    for line in squareLst:
        print(line)

def main():
    square = generate_test(5)
    print_square(square)

if __name__ == "__main__":
    main()
    
