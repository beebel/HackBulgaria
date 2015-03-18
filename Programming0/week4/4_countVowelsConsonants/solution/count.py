vowels = "aeiouy"

def vowelOrConsonant(letter):
    if letter in vowels or letter.lower() in vowels:
        return "vowel"
    else:
        return "consonat"

def oneLetterCount(word):
    counter = {'vowel': 0, 'consonant': 0}
    if vowelOrConsonant(word[0]) == "vowel":
        counter['vowel'] = counter['vowel'] + 1
    else:
        counter['consonant'] = counter['consonant'] + 1
    return counter
        
def count_vowels_consonants(word):
    result = {'vowels': 0, 'consonants': 0}
    while len(word) > 0:
        if oneLetterCount(word)['vowel'] == 1:
            result['vowels'] = result['vowels'] + 1
        else:
            result['consonants'] = result['consonants'] + 1
        word = word[1:]
    return result
        

def main():
    word = input("Enter your word: ")

    print(count_vowels_consonants(word))

if __name__ == "__main__":
    main()

