def head(lst):
    return lst[0]

def last(lst):
    return lst[-1]

def tail(lst):
    return lst[1:]

def equal_lists(lst1, lst2):
    return lst1 == lst2

def count_item(item, lst):
    return lst.count(item)

def take(n, lst):
    newList = []
    for i in range(n):
        newList.append(lst[i])
    return newList
    
def drop(n, lst):
    newList = lst[n:]
    return newList
def reverse(lst):
    return lst[::-1]
def main():
    first = input("Enter first list: ")
    firstList = first.split(" ")
    second = input("Enter second list: ")
    secondList = second.split(" ")
    element = input("Enter your element: ")
    number = input("Enter your number: ")
    number = int(number)
    
    print("first list after head func: " + str(head(firstList)))
    print("second list after head func: " + str(head(secondList)))
    print("first list after last func: " + str(last(firstList)))
    print("second list after last func: " + str(last(secondList)))
    print("first list after tail func: " + str(tail(firstList)))
    print("second list after tail func: " + str(tail(secondList)))
    print("equal_lists: " + str(equal_lists(firstList, secondList)))
    print("count_item from first list: " + str(count_item(element, firstList)))
    print("take func from first list: " + str(take(number, firstList)))
    print("drop func from first list: " + str(drop(number, firstList)))
    print("reverse func from first list: " + str(reverse(firstList)))
    print("reverse func from first list: " + str(reverse(secondList)))

if __name__ == "__main__":
    main()
