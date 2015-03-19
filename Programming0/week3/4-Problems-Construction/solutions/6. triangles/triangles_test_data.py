from random import randint

def generate_triangle_test(maxLenSide):
    result = [randint(1,maxLenSide) for n in range(3)]

    return result
    
def main():
    triangle = generate_triangle_test(10)
    print(triangle)

if __name__ == "__main__":
    main()
