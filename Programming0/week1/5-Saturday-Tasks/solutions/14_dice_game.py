import random

player1 = input("Player1 name: ")
player2 = input("Player2 name: ")

def oneRound(dicesInGame):
    sum5Dices = 0
    i = 1
    while i <= dicesInGame:
        dice = random.randint(1, 6)
        sum5Dices = sum5Dices + dice
        i = i + 1

    return sum5Dices

def printRes(name1, dices1, score1, name2, dices2, score2):
    print(name1 + " dices: " + str(dices1) + " score: " + str(score1))
    print(name2 + " dices: " + str(dices2) + " score: " + str(score2))

def game(name1, result1, name2, result2):

    counter = 2
    winner = ""
    
    while True:
        print("Round " + str(counter) + ":") 
        dices1 = oneRound(5)
        dices2 = oneRound(5)
        if result1 > 0:
            result1 = result1 - dices1
        elif result1 < 0:
            result1 = dices1 + result1
        if result2 > 0:
            result2 = result2 - dices2    
        elif result2 < 0:
            result2 = dices2 + result2
          
        printRes(name1, dices1, result1, name2, dices2, result2)

        if result1 == 0 and result2 != 0:
            winner = name1
            break
        if result1 != 0 and result2 == 0:
            winner = name2
            break
        if result1 == 0 and result2 == 0:
            winner = name1 + " and " + name2
            break
        counter = counter + 1

    print("Game Over!!!")    
    return winner

firstDices1 = oneRound(5)
firstDices2 = oneRound(5)
score1 = 1001 - firstDices1
score2 = 1001 - firstDices2

print("Round 1:")
printRes(player1, firstDices1, score1, player2, firstDices2, score2)

print("Winner: " + game(player1, score1, player2, score2))
