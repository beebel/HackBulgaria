import random

def generateTest(wideMatrix):
    ch = ["X", "O", "#"]
    result = []
    for i in range(wideMatrix):
        result.append([random.choice(ch) for n in range(wideMatrix)])

    return result

def printSquare(lst):
    for e in lst:
        print(e)
    
def main():
    board = generateTest(3)
    printSquare(board)

if __name__ == "__main__":
    main()
