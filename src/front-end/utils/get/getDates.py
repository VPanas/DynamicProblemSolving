import datetime

def getDates():
    today = datetime.date.today()
    weekday = today.isoweekday()
    # The start of the week
    start = today - datetime.timedelta(days=weekday - 1)
    # Build a simple range
    tenWeeks = 10
    dates = [start - datetime.timedelta(days=7 * i) for i in range(tenWeeks)]

    weeks = list()

    for date in reversed(dates):
        print(date, start)
        if date.day == today.day:
            print("entro")
            week = [date + datetime.timedelta(days=d) for d in range(weekday)]
        else:
            week = [date + datetime.timedelta(days=d) for d in range(7)]
        week_days = [day.day for day in week] 
        weeks.append(week_days)

    return weeks

getDates()
