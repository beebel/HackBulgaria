import random

def generate_test(maxBuildings):
    buildings = random.randint(1, maxBuildings)
    floors = [floor for floor in range(1, 15)]
    result = [random.choice(floors) for n in range(1, buildings + 1)]

    return result

def main():
    towers = generate_test(10)
    print(towers)

if __name__ == "__main__":
    main()
