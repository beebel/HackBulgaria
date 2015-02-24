score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
 
def textToList(text):
    textLst = []
    for e in text:
        textLst.append(e)
    return textLst

def oneLetterPoints(word):
    key = word[len(word) - 1]
    key = key.lower()
    if key in score:
        return score[key] 

def scrabble_score(word):
    sumPoints = 0
    while len(word) > 0:
        sumPoints = sumPoints + oneLetterPoints(word)
        word = word[:len(word) - 1]
    return sumPoints

def main():
    word = input("Enter your word: ")

    print(scrabble_score(word))

if __name__ == "__main__":
    main()
