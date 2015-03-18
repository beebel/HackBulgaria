from beers_and_fries_test import generate_test

def max_score(beers, fries):
    result = []

    for i in range(len(beers)):
        if beers[i] < 0 or fries[i] < 0:
            result.append(-(abs(beers[i]) * abs(fries[i])))
        else:
            result.append(beers[i] * fries[i])

    maxScore = sum(result)

    return maxScore

def main():
    marksBeers, marksFries = generate_test(10)
    print("marks for beer: " + str(marksBeers))
    print("marks for fries: " + str(marksFries))
    print()
    print(max_score(marksBeers, marksFries))

if __name__ == "__main__":
    main()
