def reverse(text):
    textLst = []
    result = ""
    for e in text:
        textLst.append(e)
    i = len(textLst) - 1
    while i >= 0:
        result = result + textLst[i]
        i = i - 1
    return result

def main():
    txt = input("Enter text: ")
    
    print(reverse(txt))

if __name__ == "__main__":
    main()

    
