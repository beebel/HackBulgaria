from pairs import splitInput

def count_zero_pairs(numbers):
    pairs = 0
    for number in numbers:
        if number == 0:
            pairs = 1
            break
    if len(numbers) > 1:
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] == 0:
                pairs += 1

    return pairs

def main():
    txt = input("Enter your numbers here: ")

    print(count_zero_pairs(splitInput(txt)))

if __name__ == "__main__":
    main()
