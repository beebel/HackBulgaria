def count_words(words):
    result = {}
    for e in words:
        result[e] = words.count(e)
    return result

def main():

    lst = ["words", "are", "meaningful", "words", "words", "are"]
    print(count_words(lst))

if __name__ == "__main__":
    main()
