def str_reverse(txt):
    return txt[::-1]

def startswith(search, target):
    if search == target[:len(search)]:
        return True
    else:
        return False

def endswith(search, target):
    revTarget = str_reverse(target)
    revSearch = str_reverse(search)
    return startswith(revSearch, revTarget)

def startChPos(string):
    startPos = 0
    for i in range(len(string)):
        if string[i] != ' ':
            startPos = i
            break
        
    return startPos
    

def trim(string):
    start = startChPos(string)
    end = startChPos(str_reverse(string))
    if end == 0:
        return string[start:]
    else:
        return string[start:-end]

def main():
    string = input("Enter your string: ")
    search = input("Enter your search: ")
    print("str_reverse: " + str_reverse(string))
    print("startswith: " + str(startswith(search, string)))
    print("endswith: " + str(endswith(search, string)))
    print("trim: " + "\n" + trim(string)) 

if __name__ == "__main__":
    main()
