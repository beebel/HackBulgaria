from sands_of_time_test_data import generate_test

def sands_of_time(num):
    star = '*'
    dot = '.'
    n = num
    index = 1
    while n >= 3:                                       # top
        print(index * dot + n * star +  index * dot)    
        n -= 2
        index += 1
    print(((num + 2) // 2) * dot + star + ((num + 2) // 2) * dot)  # middle
    n = 3
    index = (num + 2)// 2 - 1
    while n <= num:                                     # bottom
        print(index * dot + n * star +  index * dot)
        n += 2
        index -= 1
    print()
def main():
    num = generate_test()
    print(num)
    print()
    print(sands_of_time(num))

if __name__ == "__main__":
    main()
