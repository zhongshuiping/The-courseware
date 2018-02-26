import time
from celery import task

@task
def show():
    print('hello...')
    time.sleep(5)
    print('world...')

