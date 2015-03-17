num  = input("Enter n: ")
n = int(num)

line = "|00000*****   |"
text = ['|', '0', '0', '0', '0', '0', '*', '*',
        '*', '*', '*', ' ', ' ', ' ', '|']

if n == 0:
    while n <= 9:
        print(line)
        n = n + 1

else:
    line = ""
    prints = []

    while n > 0:
        text.insert(11 - n % 10, ' ')
        text.insert(12 - n % 10, ' ')
        text.insert(13 - n % 10, ' ')
        text.pop(-2)
        text.pop(-2)
        text.pop(-2)
        for e in text:
            line = line + e            
        prints.append(line)
        text = ['|', '0', '0', '0', '0', '0', '*', '*',
                '*', '*', '*', ' ', ' ', ' ', '|']
        line = ""
        n = (n - n % 10) // 10

    line = "|00000*****   |"       
    countPrints = len(prints)
    while countPrints < 10:
        prints.append(line)
        countPrints += 1

    prints.reverse()

    for e in prints:
        print (e)
    

    
