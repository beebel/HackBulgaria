import random

def string_matrix_test_data(minWidth, maxWidth):
    words = ["python","gogo","perl","java","haskell","ruby0nRails", "C#",
             "django", "C++", "javaScript"]
    width = random.randint(minWidth, maxWidth)
    result = []
    index = 0
    while index < width:
        choice = random.choice(words)
        if choice not in result:
            result.append(choice)
            index += 1

    return width, result
        
def main():
    print(string_matrix_test_data(2, 6))

if __name__ == "__main__":
    main()
