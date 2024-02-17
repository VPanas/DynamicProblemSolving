import datetime

def getWeeks():
    #quantity of weeks to display
    weeksNumber = 24
    # today() : 2024 02 15
    today = datetime.date.today()
    # day of the week : 4th day of the week
    weekday = today.isoweekday()
    # The start of the week : 1st day : 2024 02 12 (week ; 12,13,14,15/today,16,17,18)
    start = today - datetime.timedelta(days=weekday - 1)
    # get Current week all days till today not more (12,13,14,15/today)
    currentWeek = [start + datetime.timedelta(days=d) for d in range(weekday)]
    #first day last week
    firstDayLastWeek = start - datetime.timedelta(days=7)
    #get the week before this one (complete since its finished)
    weekBefore = [firstDayLastWeek + datetime.timedelta(days=d) for d in range(7)]
   
    #add first week and week before
    weeks = list()
    weeks.append(currentWeek)
    weeks.append(weekBefore)

    #get weeks before the week before current week
    for index in range(weeksNumber):
        firstDayLastWeek = firstDayLastWeek - datetime.timedelta(days=7)
        print(firstDayLastWeek)
        weekBefore = [firstDayLastWeek + datetime.timedelta(days=d) for d in range(7)]
        weeks.append(weekBefore)

    #reverse list
    reversed_list = list(reversed(weeks))
    print(reversed_list)
    return reversed_list
    