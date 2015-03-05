from random import randint

def generate_test(count):
    seasons = ["winter", "summer", "spring"]
    result = []
    countSummers = randint(1, count)
    result = result + [seasons[0]]
    result = result + [seasons[1]] * countSummers
    if countSummers == 3:
        result = result + [seasons[2]] * randint(1, 2)
        return result
    else:
        return result

def main():
    print(generate_test(3))

if __name__ == "__main__":
    main()
