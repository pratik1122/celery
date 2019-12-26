
from celery import shared_task
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None



import django
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse


from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.utils.timezone import timedelta


# @periodic_task(run_every=(crontab(minute='*/1')),name= 'send_email_task', ignore_result=True)



@periodic_task(run_every=timedelta(seconds=5))
def send_email_task():
    send_mail('Subject here', 'NEW TASK', settings.EMAIL_HOST_USER,
              ['pratik.mukherjee@kevit.io'], fail_silently=False)
    return None

