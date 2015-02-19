# Във файл с име books.py имате следния код:

# book1_name = "Pragmatic Thinking and Learning"
# book1_price = 30

# В файла, чрез създаване на нови променливи, с последователна номерация,
# добавете следните книги:

# Ако цената е Free, то тя се равнява на 0.

#         Книга	                Цена

# Learn You a Haskell	        Free
# The Healthy Programmer	50
# Code Complete	                60
# The Pragmatic Programmer	20
# Pro Git	                Free
# Introduction to Algorithms	80
# Concrete Mathematics	        100


book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book1_discount = 0
book1_final_price = (book1_price - (book1_discount * book1_price)/ 100)
book2_name = "Learn You a Haskell"
book2_price = 0
book2_discount = 0
book2_final_price = (book2_price - (book2_discount * book2_price)/ 100)
book3_name = "The Healthy Programmer"
book3_price = 50
book3_discount = 0
book3_final_price = (book3_price - (book3_discount * book3_price)/ 100)
book4_name = "Code Complete"
book4_price = 60
book4_discount = 0
book4_final_price = (book4_price - (book4_discount * book4_price)/ 100)
book5_name = "The Pragmatic Programmer"
book5_price = 20
book5_discount = 0
book5_final_price = (book5_price - (book5_discount * book5_price)/ 100)
book6_name = "Pro Git"
book6_price = 0
book6_discount = 0
book6_final_price = (book6_price - (book6_discount * book6_price)/ 100)
book7_name = "Introduction to Algorithms"
book7_price = 80
book7_discount = 25
book7_final_price = (book7_price - (book7_discount * book7_price)/ 100)
book8_name = "Concrete Mathematics"
book8_price = 100
book8_discount = 25
book8_final_price = (book8_price - (book8_discount * book8_price)/ 100)

# След като създаде променливите за съответните книги, в същия файл,
# използвайки print() функцията, отпечатайте следните неща:

# Изпринтете всяка книга, която е налична, заедно с нейната цена.
# Колко е сумата на всички книги?
# Колко е общия брой на всички книги?
# Ако човек вземе Introduction to Algoritims и Concrete Mathematics, получавa
# 25% намаление. Колко ще е цената тогава?
# Ако човек има бюджет от 150, колко книги най-много може да вземе?
# Кои са тези книги?


titles_and_prices = [[book1_name, book1_price, book1_discount, book1_final_price],
                     [book2_name, book2_price, book2_discount, book2_final_price],
                     [book3_name, book3_price, book3_discount, book3_final_price],
                     [book4_name, book4_price, book4_discount, book4_final_price],
                     [book5_name, book5_price, book5_discount, book5_final_price],
                     [book6_name, book6_price, book6_discount, book6_final_price],
                     [book7_name, book7_price, book7_discount, book7_final_price],
                     [book8_name, book8_price, book8_discount, book8_final_price]]

for e in titles_and_prices:
    print (str(e[0]) + ":   " + str(e[1]))

sum_all_books = 0

for e in titles_and_prices:
    sum_all_books = sum_all_books + e[1]

print ("sum all books:   " + str(sum_all_books))
print ("count all books:   " + str(len(titles_and_prices)))

print (titles_and_prices[6][0] + " with discount: " + str(titles_and_prices[6][3]))
print (titles_and_prices[7][0] + " with discount: " + str(titles_and_prices[7][3]))

money_to_spent = 150
spent = 0
i = 0
books_can_buy = []
possible = []

for e in titles_and_prices:
        spent = spent + e[3]
        if(spent > money_to_spent):
            spent = spent - e[3]
        else:
            books_can_buy.append([e[0], e[1]])
            
for e in books_can_buy:
    print (e)

========================================================

while(i < len(titles_and_prices)):
    count = i
    while(count < len(titles_and_prices)):
        spent = spent + titles_and_prices[count][3]
        if(spent > money_to_spent):
            spent = spent - titles_and_prices[count][3]
        else:
            books_can_buy.append(titles_and_prices[count][0], titles_and_prices[count][3])
        count = count + 1

    i = i + 1
