import time
import datetime
import calendar

calAge = time.time() - 1208692296

def calCulate(yB, mB, dB):
    userTuple = datetime.datetime(yearBirth, monthBirth, dayBirth, 0, 0, 0)
    userAge = time.time() - calendar.timegm(userTuple.timetuple())

    return userAge/calAge

yearBirth = int(input("Input the year you were born\n"))
monthBirth = int(input("Input the month you were born (1-12)\n"))
dayBirth = int(input("Input the day you were born (1-31)\n"))

ageDifference = calCulate(yearBirth, monthBirth, dayBirth)
print("You are " + str(ageDifference) + " cals, or " + str(ageDifference * 100) + "% cal.")
