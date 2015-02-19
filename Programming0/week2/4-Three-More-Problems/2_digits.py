num = input("Enter number n: ")
n = int(num)

digits = []

while n > 0:
    digits = digits + [n % 10]
    n = (n - (n % 10)) // 10

digits.reverse()

print("List of digits is: " + str(digits))

text = ""
for e in digits:
    text = text + str(e)

n = int(text)
print("Number is: " + str(n))
    
