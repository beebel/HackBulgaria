from lyulin_city_test_data import generate_test

def towersToSee(towers):
    count = 1
    highest = towers[0]
    for i in range(len(towers)):
        if towers[i] > highest:
            highest = towers[i]
            count += 1

    return count
        
def main():
    towers = generate_test(10)
    print(towers)
    print()
    print(towersToSee(towers))

if __name__ == "__main__":
    main()
