
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def day_in_month(year, month):
    if month > 12 or month < 1:
        return 'Invalid Month'
    month_days = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]  # Jalali
    if is_leap(year) and month == 12:
        return 30
    return month_days[month-1]


year = int(input('Please enter year : '))
month = int(input('Please enter month : '))

days = day_in_month(year, month)

print(days)
