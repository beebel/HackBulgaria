text = input("Enter first number: ")
n = int(text)
text = input("Enter second number: ")
m = int(text)

def bigger(n1, n2):
    if n1 >= n2:
        return n1
    else:
        return n2

if n % 10 > m % 10:
    result = n
elif m % 10 > n % 10:
    result = m
else:
    result = bigger(n,m)

print(result)    
