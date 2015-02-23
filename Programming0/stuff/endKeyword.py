phrase = "A bird in the hand..."

for c in phrase:
    if c == "A" or c == "a":
        print("X", end='*')
    else:
        print(c, end='')
