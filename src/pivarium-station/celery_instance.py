from celery import Celery

config = {
    "timezone": "US/Eastern",
    "mongodb_scheduler_db": "celery",
    "mongodb_scheduler_url": "mongodb://localhost:27017",
}

celery = Celery('pivarium-station', broker='amqp://localhost')

celery.conf.update(**config)
