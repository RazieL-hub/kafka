import datetime
import logging
import os
from typing import List

from fastapi import FastAPI, BackgroundTasks, Query
from starlette.responses import JSONResponse

from apps.email.schemas import EmailSchema
from apps.email.views import send_email
from apps.telegram.send_message import send_message
from core.celery import celery_app

from databases import Database

from db.table import reports

# database = Database('postgresql+asyncpg://postgres:postgres@localhost:/postgres')


log = logging.getLogger(__name__)
app = FastAPI()


# def background_on_message(task):
#     log.warn(111111111111111111)
#     log.warn(task)
#     task.wait()
#     if task.status == 'SUCCESS':
#         log.warn('URAAAAAAAAAAAAa')
#         query = reports.select()
#         values = {'name': task.id}
#         row = await database.fetch_one(query=query, values=values)

"""
def update(self, whereclause=None, values=None, inline=False, **kwargs):
    Generate an :func:`_expression.update` construct against this
    :class:`_expression.TableClause`.

    E.g.::

        table.update().where(table.c.id==7).values(name='foo')

    See :func:`_expression.update` for argument and usage information.
"""


@app.get('/{word}')
async def root(word: str, background_task: BackgroundTasks):
    database = Database('postgresql+asyncpg://postgres:postgres@localhost:5433/postgres')
    await database.connect()
    query = reports.insert()
    task_name = "core.celery.test_celery"
    await database.execute(query=query)
    await database.disconnect()

    task = celery_app.send_task(task_name, args=[word, ], eta=datetime.datetime.now() + datetime.timedelta(seconds=5))

    # background_task.add_task(background_on_message, task)


    return {"message": "Hello world"}


@app.post('/send-report')
async def send_report_asynchronous(
        type_event: str = Query(None, description='type_event'),
        users_id: List[str] = Query(None, description='Send report for users'),
        payload: str = Query(None, description='Link to file. This field required')) \
        -> JSONResponse:
    await send_message(chat_id='-1001576623026', payload=f"{payload}")
    # await send_email(EmailSchema(email=[os.getenv('MY_EMAIL')]), params={'title': 'REPORT', 'name': 'QWERTY'})
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
