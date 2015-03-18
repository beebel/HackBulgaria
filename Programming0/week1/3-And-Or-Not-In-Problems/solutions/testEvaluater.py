p = input("Enter points:  ")
p = int(p)

if (p >= 0) and (p <= 50):
    print("Слаб 2")
elif (p > 50) and (p <= 60):
    print("Среден 3")
elif (p > 60) and (p <= 70):
    print("Добър 4")
elif (p > 70) and (p <= 80):
    print("Много Добър 5")
elif (p > 80) and (p < 100):
    print("Отличен 6")
else:
    print("Много Отличен 7")
