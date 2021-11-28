import mongoengine

mongoengine.connect("celery", host='localhost:27017')