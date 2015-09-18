num_days_per_month           = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num_days_per_month_leap_year = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    
    for y in range(year1, year2 + 1):
        days += days_in_year(y)

    days = days - days_from_jan1(year1, month1, day1) - days_to_dec31(year2, month2, day2)
    
    # print days
    return days

def days_in_year(year):
    if is_leap_year(year):
        days = 366
    else:
        days = 365

    return days

            
def days_from_jan1(year, month, day):
    days = 0
    if is_leap_year(year):
        for m in range(month):
            days += num_days_per_month_leap_year[m]

        days = days - (num_days_per_month_leap_year[month - 1] - day)        
    else:
        for m in range(month):
            days += num_days_per_month[m]

        days = days - (num_days_per_month[month - 1] - day)

    return days    


def days_to_dec31(year, month, day):
    days = 0
    if is_leap_year(year):
        for m in range(month - 1, 12):
            days += num_days_per_month_leap_year[m]

        days = days - day

    else:
        for m in range(month - 1, 12):
            days += num_days_per_month[m]

        days = days - day
        
    return days    


    
def is_leap_year(year):
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
