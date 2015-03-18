text = input("Enter text: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E',
          'I', 'O', 'U', 'Y']

index = 0
sumVow = 0

while index < len(vowels):
    sumVow = sumVow + text.count(vowels[index])
    index += 1

print("Counted vowels: " + str(sumVow))    
