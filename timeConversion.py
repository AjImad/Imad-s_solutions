# Problem link: https://www.hackerrank.com/challenges/time-conversion

def timeConversion(time):
    period = time[-2:]
    hour, minute, second = time[:-2].split(":")

    if period == "AM":
        if hour == "12":
            hour = "00"
    else:
        hour = str(int(hour) + 12)
    
    return f"{hour}:{minute}:{second}"