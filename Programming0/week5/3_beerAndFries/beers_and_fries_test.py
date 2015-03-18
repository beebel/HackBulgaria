import random

def generate_test(marks):
    maxMark = 1040
    minMark = -maxMark
    allMarks = [i for i in range(minMark, maxMark + 1)]
    beersMarks = []
    friesMarks = []
    for i in range(random.randint(1, marks)):
        beersMarks.append(random.choice(allMarks))
        friesMarks.append(random.choice(allMarks))
    beersMarks.sort()
    friesMarks.sort()
    return beersMarks, friesMarks

def main():
    print(generate_test(10))

if __name__ == "__main__":
    main()
