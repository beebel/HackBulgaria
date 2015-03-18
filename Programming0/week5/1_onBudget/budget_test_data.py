from random import randint

def generate_test(maxCountBooks, maxPrice):
    books = []
    budget = randint(0, maxPrice)
    countBooks = randint(1, maxCountBooks)
    for i in range(countBooks):
        books = books + [randint(0, maxPrice)]

    books.sort()
    return books, budget
    
    
def main():
    print(generate_test(10, 100))

if __name__ == "__main__":
    main()
