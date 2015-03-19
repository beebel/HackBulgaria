def fib_number(n):
    result = [1, 1]
    if n == 1:
        result.pop()
    elif n == 2:
        None
    else:
        for i in range(2, n):
            nextNum = result[i - 2] + result[i - 1]
            result.append(nextNum)

    return result

def printResultAsOneNum(lst):
    for e in lst:
        print(e, end="")

def main():
    num = input("Enter n:  ")
    num = int(num)
    printResultAsOneNum(fib_number(num))

if __name__ == "__main__":
    main()
