# Celery Example

## Docs

- Celery cannot work in isolation and requires the use of a message broker service. It uses this to send and receive messages.

- A message can be any kind of information; in Celery’s case, a message is a task. Messages are managed by the message broker service via queues.

- The message broker queue will store a message until it is consumed by one of Celery’s worker processes. Once consumed, the message is removed from the queue.

