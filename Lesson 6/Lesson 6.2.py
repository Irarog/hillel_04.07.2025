seconds_input = int(input("Enter seconds, 0 <= seconds < 8640000: "))

seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour

#count days, hrs, min and sec
days, remainder = divmod(seconds_input, seconds_in_day)
hours, remainder = divmod(remainder, seconds_in_hour)
minutes, seconds = divmod(remainder, seconds_in_minute)

#function for days word
def day_word(day: int) -> str:
    if day == 1:
        return 'день'
    elif 2 <= day <= 4:
        return 'дні'
    else:
        return 'днів'

# print days, hrs, min and sec
print(f"{days} {day_word(days)}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")