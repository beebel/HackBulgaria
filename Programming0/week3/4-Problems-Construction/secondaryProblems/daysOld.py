# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthsLeap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isDateBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            if day1 <= day2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def isLeapYear(year, month, day):
    result = False
    if year % 4 == 0:
        result = True
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
            else:
                result = False
    return result       
                
                
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    """
    day = day + 1
    if isLeapYear(year, month, day):
        if day > daysOfMonthsLeap[month - 1]:
            day = 1
            month = month + 1
            if month > 12:
                month = 1
                year = year + 1     
    else:
        if day > daysOfMonths[month - 1]:
            day = 1
            month = month + 1
            if month > 12:
                month = 1
                year = year + 1
    return year, month, day                
                
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert isDateBefore(year1, month1, day1, year2, month2, day2)
    days = 0
    while isDateBefore(year1, month1, day1, year2, month2, day2):
        if year1 == year2 and month1 == month2 and day1 == day2:
            break
        year1, month1, day1 = nextDay(year1, month1, day1)
        days = days + 1
    return days                



def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((1984,9,12,2015,2,23), 11121)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print(result)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()
