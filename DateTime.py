import datetime


def getDate():
    r = datetime.datetime.now()
    date = r.date()
    return date


def getTime():
    r = datetime.datetime.now()
    time = r.strftime("%H:%M")
    return time
