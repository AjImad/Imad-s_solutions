# Problem link: https://www.hackerrank.com/challenges/day-of-the-programmer

def dayOfProgrammer(year):
    months_days_number = {
    "jan": 31,
    "feb": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "aug": 31
    }

    def daysSum(months_days):
        days_sum = 0
        for _, value in months_days_number.items():
            days_sum += value
        return 256 - days_sum

    if year == 1918:
        months_days_number['feb'] = 15
        return f"{daysSum(months_days_number)}.09.{year}"
    elif (year <= 1917 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        months_days_number['feb'] = 29
        return f"{daysSum(months_days_number)}.09.{year}"
    else:
        return f"{daysSum(months_days_number)}.09.{year}"