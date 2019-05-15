# Simple Celery Example

## Docs

- Celery cannot work in isolation and requires the use of a message broker service. It uses this to send and receive messages.

- A message can be any kind of information; in Celery’s case, a message is a task. Messages are managed by the message broker service via queues.

- The message broker queue will store a message until it is consumed by one of Celery’s worker processes. Once consumed, the message is removed from the queue.


## Asynchronous Processing in Celery

- [main.py](./main.py) - Showcases an ordinary implementation of a time consuming operation.
- [task.py](./task.py) - This example implements main.py above in an asycnhronous manner using Celery.

```shell
celery -A task worker --loglevel=info
```

## Periodic Tasks in Celery

- [periodic.py](./periodic.py) - This example implements a timed periodic task that runs after every two seconds.

```shell
celery -A periodic beat --loglevel=info
rabbitmqctl list_queues

# discard all the messages in the celery queue
rabbitmqctl purge_queue celery
# verify the purge
rabbitmqctl list_queues
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
celery 0
```

Workers, as the name suggests, do the important work of consuming messages from a queue. Once they consume a message successfully, that message is taken off the queue by the message broker.

You may have noticed that the celery beat service is running on the MainProcess as it sends the periodic.see_you task to the message broker.

```shell
celery -A periodic worker --loglevel=info
```

## Crontabs in Celery

- [birthdays.py][./birthdays.py] - This example implements a birthday notification system using Celery's crontab feature.
