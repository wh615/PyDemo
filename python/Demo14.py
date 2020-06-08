from datetime import datetime

if __name__ == '__main__':
    date = datetime.now();  ##获取当前datetime
    print(date)
    print(date.date())
    print(date.year,date.month,date.day,date.hour)
    print(type(date))
    print(datetime(2019, 12, 30, 19, 28, 13))
    t=datetime(2019, 12, 30, 19, 28, 13).timestamp();
    print(datetime.fromtimestamp(t))

