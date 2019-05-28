import datetime

currentDate = datetime.date(1901, 1, 6)
oneDay = datetime.timedelta(days=1)

counter = 0
while currentDate < datetime.date(2000, 12, 31):
    if currentDate.weekday() is 6 and currentDate.day is 1:
        counter += 1
    currentDate += oneDay

print(counter)
