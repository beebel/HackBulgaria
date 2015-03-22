from string_matrix_test_data import string_matrix_test_data

def string_matrix(matrix_width, strings):
    width, words = matrix_width, strings 

    result = ""
    for i in range(width):
        result += "| "
        if len(words[i]) < width:
            result += ' | '.join(words[i] + (width - len(words[i])) * 'X')
        elif len(words[i]) > width:
            result += ' | '.join(words[i][: width])
        else:
            result += ' | '.join(words[i])
        result += ' |\n'

    return result

def main():
    inpt = string_matrix_test_data(2, 6)
    width, words = inpt
    print(inpt)
    print()
    print(string_matrix(width, words))

if __name__ == "__main__":
    main()
