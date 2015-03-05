from people_count_test_data import generate_test

def get_people_count(activity):
    names = []
    for name in activity:
        if name not in names:
            names.append(name)

    return len(names)

def main():
    names = generate_test(4)
    print(names)
    print(get_people_count(names))

if __name__ == "__main__":
    main()
