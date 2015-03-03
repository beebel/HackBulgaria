def calculate_coins(sum):
    coins = [1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    result = {}
    num = sum
    
    for coin in coins:
        if num >= coin:
            result[coin] = int(num // coin)
            num = round(num % coin, 2)
        else:
            result[coin] = 0

    return result
            
    
def main():
    num = input("Enter your number here: ")
    num = float(num)

    print(calculate_coins(num))

if __name__ == "__main__":
    main()
