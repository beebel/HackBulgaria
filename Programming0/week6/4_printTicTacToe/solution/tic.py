from board_to_string_test import generateTest
from board_to_string_test import printSquare

def board_to_string(board):

    result = ""
    for e in board:
        result += "| "
        result += ' | '.join(e)
        result += ' |\n'
    return result
    
def main():
    board = generateTest(3)
    printSquare(board)
    print()
    print(board_to_string(board))

if __name__ == "__main__":
    main()
