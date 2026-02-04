
def time_now():
    """ keep asking until we get valid integer input for hours and minutes"""
    while True:
        hours_str = input("please enter what hour it is right now ")
        try:
            hours = int(hours_str)
            break
        except ValueError:
            print("ERROR: enter valid integer")

    while True:
        minutes_str = input("please enter the current minute it is now ")
        try:
            minutes = int(minutes_str)
            break
        except ValueError:
            print("ERROR: please enter an integer value")

    return hours, minutes

def time_advance():
    """ keep asking until we get valid integer input for hours and minutes"""
    while True:
        hours_advance_str = input("please enter what hour it is right you want to go forward ")
        try:
            hours_advance = int(hours_advance_str)
            break
        except ValueError:
            print("ERROR: enter valid integer")

    while True:
        minutes_advance_str = input("please enter the current minute it is you want to go forward  ")
        try:
            minutes_advance = int(minutes_advance_str)
            break
        except ValueError:
            print("ERROR: please enter an integer value")

    return hours_advance, minutes_advance

hours, minutes = time_now();
hours_advance, minutes_advance = time_advance();

day = 0
alarm_hours = hours + hours_advance
alarm_minutes = minutes + minutes_advance
while alarm_minutes >= 60:
    alarm_minutes -= 60
    alarm_hours += 1
while alarm_hours >= 24:
    alarm_hours -= 24
    day += 1

print(f"your alarm will go off at {day} days {alarm_hours} hours {alarm_minutes}  time ")