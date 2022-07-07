import datetime

def Date():
    d = datetime.datetime.now
    return str(d().date())

def Time():
    t = datetime.datetime.now
    return str(t().time())