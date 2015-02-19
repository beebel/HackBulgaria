from prime_digit import to_digits

def bigger(a, b):
    if a >= b:
        return a
    else:
        return b

def smallestPossible(nums):

    biggest = 9
    indexPosSmallest = 0
    smallestArrange = []
    i = 0
    while i < len(nums):
        if nums[i] < biggest:
            biggest = nums[i]
            indexPosSmallest = i
            
        smallestArrange.append(nums[i])
        i = i + 1

    return smallestArrange

def largestPossible(nums):

    smallest = 0
    indexPosBiggest = 0
    biggestArrange = []
    i = 0
    while i < len(nums):
        if nums[i] > smallest:
            smallest = nums[i]
            indexPosBiggest = i
            
        biggestArrange.append(nums[i])
        i = i + 1

    return biggestArrange

def printNumber(list):
    text = ""
    for e in list:
        text = text + str(e)

    return text

def main():
    n = input("Enter n: ")
    nDigitsList = to_digits(n)

    largest = largestPossible(nDigitsList)
    smallest = smallestPossible(nDigitsList)
    
    print(largest)#"Lagest: %d" % 
    print(smallest)#"Smallest: %d" % 


if __name__ == "__main__":
    main()
    
