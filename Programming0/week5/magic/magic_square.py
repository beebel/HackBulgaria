from magic_square_test import generate_test
from magic_square_test import print_square

def magic_square(square):
    result = True
    magicSum = sum(square[0])
    
    for i in range(len(square)):  # check for rows
        sumTemp = sum(square[i])
        if sumTemp != magicSum:
            result = False
            break
        
    if result:          # check for columns
        sumTemp = 0
        for j in range(len(square)):
            for i in range(len(square)):
                sumTemp = sumTemp + square[i][j]
            if sumTemp != magicSum:
                result = False
                break
            else:
                sumTemp = 0
                
    if result:           # main diagonal
        sumTemp = 0
        for i in range(len(square)):
            sumTemp = sumTemp + square[i][i]
        if sumTemp != magicSum:
            result = False
            
    if result:           # for second diagonal
        sumTemp = 0
        i = 0
        j = len(square) - 1
        while i < len(square):
            sumTemp = sumTemp + square[i][j]
            i += 1
            j -= 1
        if sumTemp != magicSum:
            result = False

    return result
                
def main():
    #square = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ] quick test for TRUE magic square
    square = generate_test(5)
    print_square(square)
    print()
    print(magic_square(square))
    

if __name__ == "__main__":
    main()

