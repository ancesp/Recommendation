import random
from datetime import datetime


class date_generation:

    def get_generated_date():
        month = random.randint(1, 12)
        print(month)

        if (month == 4 | month == 6 | month == 9 | month == 11):
            print("new random")
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 31)

        if(month == 2):
            day = random.randint(1, 29)

        year = 2020
        hour = random.randint(8, 19)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        if(day < 10):
            day = "0" + str(day)

        if(month < 10):
            month = "0" + str(month)

        if (hour < 10):
            hour = "0" + str(hour)

        if(minute < 10):
            minute = "0" + str(minute)

        if(second < 10):
            second = "0" + str(second)

        date_string = str(day) + "/" + str(month) + "/" + str(year) + \
            " " + str(hour) + ":" + str(minute) + ":" + str(second)

        print(date_string)

        date = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")

        return [date, date_string]
