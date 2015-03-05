from budget_test_data import generate_test

def on_budget(books, budget):
    result = {}
    count = 0
    bought = 0
    if sum(books) >= budget:
        loan = sum(books) - budget
    else:
        loan = 0
    for book in books:
        if bought + book <= budget:
            count += 1
            bought += book
        else:
            break
    result["books_on_budget"] = count
    result["loan"] = loan

    return result
        
def main():
    books_test, budget_test  = generate_test(10, 100)
    print("books prices':  " + str(books_test))
    print("budget:  " + str(budget_test))
    print(on_budget(books_test, budget_test))

if __name__ == "__main__":
    main()
    
