from calendar import *
import datetime

def days_passed(year, month, day):
    date = str(datetime.date.today())           # get current date
    curr_year = int(date[:4])                   # break into year, month, day
    curr_month = int(date[5:7])
    curr_day = int(date[8:])
    cal = Calendar(curr_year)                   # generate a calendar object
    print(curr_year, curr_month, curr_day)
    #curr_month = 
    year_diff = int(curr_year) - year           # get years/months/days different
    month_diff = int(curr_month) - month
    day_diff = int(curr_day) - day
    print(year_diff, "   ", month_diff, " {}".format(day_diff))
    years = range(year + 1, curr_year)          # loop through number of whole years passed
    print(years)
    years_days = 0                              # days contained within complete years
    for year_ in years:
        if isleap(year_):
            years_days += 366
            print(year_)
        else:
            years_days += 365
            
    print(years_days)
    # if january or february, check if its a leap year
    old_year_days = 0
    new_year_days = 0
    print()
    for month_ in range(month + 1, 13):     # get days in the OG year
        print(month_)
        lst = cal.itermonthdays2(year, month_)
        for pair in lst:
            print(pair)
            if pair[0] != 0:
                old_year_days += 1
                
    print(old_year_days)
    
    lst = cal.itermonthdays2(year, month)   # get days passed in month of old year
    real_days = []
    for pair in lst:
        if pair[0] != 0:
            real_days.append(pair)
    old_year_days += len(real_days) - day + 1
    
    print(old_year_days)
    
    for month_ in range(1, curr_month):     # get days passed in current year
        lst = cal.itermonthdays2(year, month_)
        for pair in lst:
            if pair[0] != 0:
                new_year_days += 1
                
    new_year_days -= 1
    print(new_year_days)
    print(curr_day)
    new_year_days += curr_day - 1
    if curr_month > 2:                      # check if this year was a leap year
        if isleap(curr_year):
            print("here")
            new_year_days += 1
            
    print("CURR: ", new_year_days)
    print("OLD: ", old_year_days)
    print("BETWEEN: ", years_days)
    return years_days + old_year_days + new_year_days
        
print(days_passed(2010, 1, 1))
