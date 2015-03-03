import re
def splitInput(inp):
    result = re.split("\W+", inp)
    return result[:-1]

def count_words(words):
    result = {}
    for e in words:
        result[e] = words.count(e)
    return result

def main():
    text = input("Enter your text: ")

    lst = ["words", "are", "meaningful", "words", "words", "are"]
    print(count_words(splitInput(text)))

if __name__ == "__main__":
    main()
