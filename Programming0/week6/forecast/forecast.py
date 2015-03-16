from forecast_testData import forecast_test

def forecast(lst):
    forecast = ""
    sunshine = lst.count("sunshine")
    rain = lst.count("rain")
    snow = lst.count("snow")

    if sunshine > rain and sunshine > snow:
        forecast = "sunshine"
    elif rain > sunshine and rain > snow:
        forecast = "rain"
    elif snow > sunshine and snow > rain:
        forecast = "snow"
    elif sunshine == rain and sunshine > snow:
        forecast = "snow"
    elif sunshine == snow and sunshine > rain:
        forecast = "rain"
    elif snow == rain and snow > sunshine:
        forecast = "sunshine"
    elif sunshine == rain and sunshine == snow:
        forecast = lst[-1]

    return forecast

def main():
    days = forecast_test(10)
    print(days)
    print()
    print(forecast(days))

if __name__ == "__main__":
    main()
