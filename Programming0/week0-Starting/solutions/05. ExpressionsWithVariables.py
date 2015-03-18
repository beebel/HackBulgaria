# В Python REPL по ваш избор (IDLE / Python Command Line),
# дефинирайте следните променливи:

first_name = "Hristo"
second_name = "Sivov"
sum = 500
discount = 0.25
base = 2
exponent = 10

# Използвайки променливите, напишете изрази, които отговарят на следните неща:

# Цялото име на човек, с интервал между първото и второто.

full_name = first_name + " " + second_name 
print (full_name)

# Колко е сумата sum, след приложеното намаление discount

print ((discount * sum)/100)

# Какво става, когато умножим цялото име на човек (с интервал по средата),
# с резултатa от base ** exponent ?

print (full_name * base ** 10)

# Как може да превърнем sum в отрицателно число?

sum = -sum
print (sum)

# Как може да превърнем превърнатото отрицателно число отгоре,
# отново в положително?

sum = -sum
print (sum)
