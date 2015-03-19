from int_functions_test_data import randInt

def reverse_int(n):
    result = str(n)[::-1]

    return int(result)

def sum_digits(n):
    sum = 0
    strN = str(n)
    for e in strN:
        sum += int(e)

    return sum

def product_digits(n):
    product = 1
    strN = str(n)
    for e in strN:
        product *= int(e)

    return product
        
def main():
    n = randInt(1000)
    print(n)
    print()
    print("reverse n: " + str(reverse_int(n)))
    print("sum digits n: " + str(sum_digits(n)))
    print("product digits n: " + str(product_digits(n)))

if __name__ == "__main__":
    main()
