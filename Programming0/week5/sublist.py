def sublist(target, search):
    #matches = []
    result = False
    if len(search) == 0:
        return True
    elif len(search) > len(target):
        return False
    else:
        for i in range(len(target)):
            if target[i] == search[0] and target[i:i+len(search)] == search:
                #matches.append(search)
                result = True
                break       #del line to operate with matches found

    return result

def main():
    target = input("Enter first list: ")
    targetList = target.split(" ")
    search = input("Enter second list: ")
    searchList = search.split(" ")
    print(sublist(targetList, searchList))

if __name__ == "__main__":
    main()
