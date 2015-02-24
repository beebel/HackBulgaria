def textToList(text):
    textLst = []
    for e in text:
        textLst.append(e)
    return textLst

def textLstToText(lst):
    text = ""
    for e in lst:
        text = text + e
    return text
    
def anti_vowel(text):
    textLst = textToList(text)
    vowels = ["a", "e", "i", "o", "u",
              "A", "E", "I", "O", "U"]
    i = 0
    for i in range(len(textLst)):
        if textLst[i] in vowels:
            textLst[i] = ""
    return textLstToText(textLst)


def main():
    txt = input("Enter your text: ")

    print(anti_vowel(txt))

if __name__ == "__main__":
    main()
