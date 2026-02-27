import calendar
import datetime
import pandas as pd
import numpy as np
import calplot
import matplotlib.pyplot as plt
import re

def highlight_dates(year, month, went_in_office):
    # ANSI codes for red and resetting
    RED, GREEN, END = '\033[91m', '\033[32m', '\033[0m'
    
    cal_str = calendar.month(year, month)
    num_days = calendar.monthrange(year, month)[1]

    total_valid_days_in_month = 0

    for day in range(1, num_days + 1):
        global total_valid_days_in_year
        weekday = calendar.weekday(year, month, day)

        if weekday == calendar.TUESDAY or weekday == calendar.WEDNESDAY or weekday == calendar.THURSDAY:
            color = RED
            
            if day in went_in_office[month]:
                color = GREEN
            
            # if day is last day of the month
            if day == num_days:
                cal_str = cal_str.replace(f' {day}', f' {color}{day}{END} ', 1)
            else:
                cal_str = cal_str.replace(f' {day} ', f' {color}{day}{END} ', 1)

            total_valid_days_in_year += 1
            total_valid_days_in_month += 1

    print(f'There are {total_valid_days_in_month} total valid days in {calendar.month_name[month]}.\n')

    return cal_str

def calculate_valid_days_left(current_date, end_date):
    count = 0

    current_date = datetime.datetime.today().date()

    while current_date <= end_date:
        weekday = current_date.weekday()
        if weekday == calendar.TUESDAY or weekday == calendar.WEDNESDAY or weekday == calendar.THURSDAY:
            count += 1
        current_date += datetime.timedelta(days=1)

    return count 

def main():
    year = 2026
    global total_valid_days_in_year
    total_valid_days_in_year = 0

    current_date = datetime.datetime.today().date()
    end_date = datetime.date(2026, 12, 31) 
    
    days_left = calculate_valid_days_left(current_date=current_date, end_date=end_date)
    
    went_in_office = {1:[22,27,28,29], 2:[3,4,5,10,11,12,18,19,26], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}

    for i in range(1, 13):
        print(highlight_dates(year, i, went_in_office))
    
    print("---------------------------------------------------------------------------------------------------")
    print("Summary:")
    print(f'There are {days_left} out of {total_valid_days_in_year} valid days left in the year.')
    print(f'Total in-person office days I currently have vs needed: {len(went_in_office)}/110')
    print(f'I need {(110 - len(went_in_office))} days left which is under {days_left}.')
    print("There are 6 upcoming holidays that may or may not fall under one of those days")

main()