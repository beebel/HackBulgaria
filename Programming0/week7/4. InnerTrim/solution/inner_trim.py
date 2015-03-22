import re

def inner_trim(string):
    result = re.split("\W+", string)
    if result[0] == '':
        del result[0]
    if result[len(result) - 1] == '':
        del result[len(result) - 1]
        
    result = " ".join(result)

    return result

def main():
    txt = input("Enter your text:  ")
    print(inner_trim(txt))

if __name__ == "__main__":
    main()
