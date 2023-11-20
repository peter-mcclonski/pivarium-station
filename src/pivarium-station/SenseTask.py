from celery_instance import celery as app

from src.app.Api import sendStatus
from Util import extFromConfig


@app.task
def sense(config: dict):
    print(config)
    sensor = extFromConfig(config)
    stat = sensor.getStatus()
    if stat is not None:
        sendStatus(stat)
