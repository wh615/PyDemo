import time

import schedule


def job():
    print("学习python")
schedule.every(0.1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)