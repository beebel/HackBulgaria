word = input("Enter word: ")
num = input("Enter n: ")
n = int(num)

count = 1
words = []

while count <= n:
    text = input()
    words.append(text)

    count += 1

print(word + " is found " + str(words.count(word)) + " times")    
