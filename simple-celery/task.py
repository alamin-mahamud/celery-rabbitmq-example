import time
from celery import Celery

BROKER_URI = "pyamqp://admin:mypass@localhost//"

app = Celery(
    "task",
    broker=BROKER_URI
)

@app.task
def sleep_asynchronously():
    time.sleep(5)
    print('5 Second Passed')
    time.sleep(5)
    print('5 Second Passed')

print("let's begin")
sleep_asynchronously.delay()
print("... and finished..")
