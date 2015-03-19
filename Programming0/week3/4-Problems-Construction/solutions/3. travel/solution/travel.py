from travel_test_data import generate_test

def travel_cost(travels):
    result = 0
    for e in travels:
        if e > 23:
            result += 23
        else:
            result += e
    if result > 50:
        result = 50

    return result
    

def main():
    travels = generate_test(5)
    print(travels)
    print()
    print(travel_cost(travels))

if __name__ == "__main__":
    main()
