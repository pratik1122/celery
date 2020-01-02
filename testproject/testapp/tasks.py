from celery import shared_task
from time import sleep
#
#
# @shared_task
# def sleepy(duration):
#     sleep(duration)
#     return None


import django
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse


from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.utils.timezone import timedelta
import celery



#@periodic_task(run_every=(crontab(minute='*/1')),name= 'send_email_task', ignore_result=True)

#
# @shared_task
# def send_email_task():
#     send_mail('Subject here', 'NEW TASK', settings.EMAIL_HOST_USER,
#               ['pratik.mukherjee@kevit.io'], fail_silently=False)
#     return None
#
#
# from django.http import HttpResponse
# @shared_task
# def get_response():
#     return HttpResponse('<h3> The raw is very good</h3>')

from kombu.common import Broadcast
from celery.schedules import crontab


import celery


@celery.task(name='message1')
def message1():
    print('this is message 1')



@celery.task(name='message2')
def message2():
    print('this is message 2')
