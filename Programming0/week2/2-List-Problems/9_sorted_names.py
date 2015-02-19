num = input("Enter n: ")
n = int(num)

count = 1
words = []

while count <= n:
    text = input()
    words.append(text)

    count += 1

words.sort()
print("Sorted names are:")
for e in words:
    print (e)
