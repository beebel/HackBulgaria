from winter_test_data import generate_test

def winter_is_coming(seasons):
    if seasons.count("spring") == 2:
        return True
    else:
        return False

def main():
    seasons = generate_test(3)
    print(seasons)
    print(winter_is_coming(seasons))

if __name__ == "__main__":
    main()
