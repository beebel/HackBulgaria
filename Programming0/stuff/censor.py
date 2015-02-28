def censor(text, word):
    listWords = text.split()
    for i in range(len(listWords)):
        if listWords[i] == word:
            listWords[i] = len(word) * "*"
    str = " "
    text = str.join(listWords)
    return text

def main():
    txt = input("Enter your text here: ")
    censored = input("Enter the word you want to be censored: ")
    
    print(censor(txt, censored))

if __name__ == "__main__":
    main()
