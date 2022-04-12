from celery import Celery

from db.table import reports

celery_app = Celery("worker", backend="rpc://user:bitnami@rabbitmq:5672//",
                    broker="amqp://user:bitnami@rabbitmq:5672//")
celery_app.conf.update(task_track_started=True)




@celery_app.task(acks_late=True)
def test_celery(word: str, task_record_id: int) -> str:
    # TODO update row in sql

    return f"test task return {word}"
