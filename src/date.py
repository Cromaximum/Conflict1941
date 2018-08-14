import random


def print_date_c(date):
    print("")
    print(str(date.time) + ":00 " + date.month + " " + str(date.day) + " " + str(date.year))
    print("")
    print("-----------")
    print("")

def next_hour(date):
    if date.time == 24:
        if date.month == "June" and date.day == 30:
            date.month = MONTHS[1]
            date.day = 1
            date.time = 0
        elif date.month == "July" and date.day == 31:
            date.month = MONTHS[2]
            date.day = 1
            date.time = 0
        elif date.month == "August" and date.day == 31:
            date.month = MONTHS[3]
            date.day = 1
            date.time = 0
        elif date.month == "September" and date.day == 30:
            date.month = MONTHS[4]
            date.day = 1
            date.time = 0
        elif date.month == "October" and date.day == 31:
            date.month = MONTHS[5]
            date.day = 1
            date.time = 0
        elif date.month == "November" and date.day == 30:
            date.month = MONTHS[5]
            date.day = 1
            date.time = 0
    else:
        date.time += 1

def random_starting_date(date):
    date.month = random.choice(MONTHS)
    date.day = random.randint(0,30)
    date.time = random.randint(0,24)

MONTHS = ['June','July','August','September','October','November']

class date:
    time = 0
    day = 22
    month = MONTHS[0]
    year = 1941