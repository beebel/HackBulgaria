import random

def forecast_test(maxDays):
    weаther = ["sunshine", "rain", "snow"]
    result = []

    days = random.randint(1, maxDays)
    for i in range(days):
        result.append(random.choice(weаther))
    
    return result

def main():
    print(forecast_test(10))

if __name__ == "__main__":
    main()
