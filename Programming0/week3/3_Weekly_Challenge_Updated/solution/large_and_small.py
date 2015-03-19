def nToDigitsPosList(num):
    listDigits = []
    if num == 0:
        listDigits.append(num)
    while num > 0:
        listDigits.append(num % 10)
        num = (num - num % 10) // 10
    listDigits.reverse()
    return listDigits

def smallestPossible(num):
    result = []
    listNum = nToDigitsPosList(num)
    lengthNum = 0
    stop = len(listNum)
    while lengthNum < stop:
        i = 0
        while i <= 9:
            if i in listNum:
               listNum.remove(i)
               result = result + [i]
               i = 9
            i += 1
        lengthNum += 1
    return result

def largestPossible(num):
    result = []
    listNum = nToDigitsPosList(num)
    lengthNum = 0
    stop = len(listNum)
    while lengthNum < stop:
        i = 9
        while i >= 0:
            if i in listNum:
               listNum.remove(i)
               result = result + [i]
               i = 0
            i -= 1
        lengthNum += 1
    return result

def returnNum(list):
    result =""
    for e in list:
        result = result + str(e)
    num = int(result)
    return num

def main():
    n = input("Enter n: ")
    n = int(n)

    largest = returnNum(largestPossible(n))
    smallest = returnNum(smallestPossible(n))
    
    print("Lagest: %d" % largest)
    print("Smallest: %d" % smallest)


if __name__ == "__main__":
    main()
    
