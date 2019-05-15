from celery import Celery

BROKER_URI = "pyamqp://admin:mypass@localhost:5672//"
app = Celery(
    'periodic',
    broker=BROKER_URI,
)

@app.task
def see_you():
    print("See you in 2 seconds")


app.conf.beat_schedule = {
    "see-you-in-two-seconds-task": {
        "task": "periodic.see_you",
        "schedule": 2.0
    }
}
