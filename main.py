import datetime
import logging

from fastapi import FastAPI, BackgroundTasks

from core.celery import celery_app

log = logging.getLogger(__name__)
app = FastAPI()


# def celery_on_message(body):
#     log.warn(222222222222, str(body))


def background_on_message(task):
    # log.warn(111111111111111111, task.get(on_message=celery_on_message, propagate=False))
    log.warn(111111111111111111)
    log.warn(task.wait())
    if task.status == 'SUCCESS':
        log.warn('URAAAAAAAAAAAAa')

@app.get('/{word}')
async def root(word: str, background_task: BackgroundTasks):
    task_name = "core.celery.test_celery"
    task = celery_app.send_task(task_name, args=[word], eta=datetime.datetime.now() + datetime.timedelta(seconds=10))
    # print(task)
    aaa = background_task.add_task(background_on_message, task)
    print(aaa)
    return {"message": "Hello world"}
