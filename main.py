import datetime
import logging
from typing import List

from fastapi import FastAPI, Query, Depends
from sqlalchemy import text
from starlette.responses import JSONResponse
from apps.telegram.send_message import send_message
from core.celery import celery_app
from db.querys import create_query as create_report

from db.database_async import Session, get_session
from db.schemas import ReportSchema

log = logging.getLogger(__name__)
app = FastAPI()


@app.get('/test_mailer_sent')
async def root(db: Session = Depends(get_session)):
    query = text(create_report).bindparams(**ReportSchema().dict())
    q = await db.execute(query)
    await db.commit()
    last_task = q.first()
    task_name = "core.celery.test_celery"
    celery_app.send_task(task_name, args=[last_task.id],
                         eta=datetime.datetime.now() + datetime.timedelta(seconds=30))
    return {"message": "Hello world"}