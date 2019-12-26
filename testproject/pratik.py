from celery.decorators import task
from datetime import datetime
import datetime
from celery import shared_task

#@task(name="sum_two_numbers")
@shared_task
def add(x, y):
    return x + y


print(add.delay(1,2))
print(add.apply_async((1, 2), expires=60)) # expires after 60 seconds
print(add.apply_async(countdown=60, expires=120)) # execute after 1 min and expires after  2 minutes


print(add.apply_async(expires= datetime.datetime.now() + datetime.timedelta(seconds=10)))
print(add.apply_async(countdown = 120 , expires = datetime.datetime.now() + datetime.timedelta(days=9,hours =1)))



from celery.task.schedules import crontab
from celery.decorators import periodic_task

clear


@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
def some_task(a,b):
    return a+b

print(some_task(2,9))
