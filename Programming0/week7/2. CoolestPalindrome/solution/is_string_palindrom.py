def spliter(string):
    
    spliter = [",", ".", "!", "?", " "]
    string = list(string)
    result = [ch for ch in string if ch not in spliter]
   
    return result

def is_string_palindrom(string):
    result = string.lower()
    inpt = string.lower()
    
    result = spliter(result)
    inpt = spliter(inpt)
    if result[::-1] == inpt:
        return True
    else:
        return False

def main():
    txt = input("Enter text or word:  ")
    print(is_string_palindrom(txt))

if __name__ == "__main__":
    main()
