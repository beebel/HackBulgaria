def splitInput(inp):
    inp = inp.split(",")
    result = []
    for i in range(len(inp)):
        result.append(int(inp[i]))
    return result
  

def count_zero_neighbours(numbers):
    pairs = 0
    if len(numbers) > 1:
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] == 0:
                pairs += 1

    return pairs

def main():
    txt = input("Enter your numbers here: ")

    print(count_zero_neighbours(splitInput(txt)))

if __name__ == "__main__":
    main()
