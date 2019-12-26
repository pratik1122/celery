from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from testapp.tasks  import sleepy,send_email_task
from celery import shared_task




from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse


def index(request):
    send_email_task.delay()
    return HttpResponse('<h2> MAIL SEND now </h2>')



#
#
# #@task(name="sum_two_numbers")
# @shared_task
# def add(x, y):
#     return x + y
#
#
#
# print(add.delay(1,2))
# print(add.apply_async((1, 2), expires=60)) # expires after 60 seconds
# print(add.apply_async(countdown=60, expires=120)) # execute after 1 min and expires after  2 minutes
#
#
# print(add.apply_async(expires= datetime.datetime.now() + datetime.timedelta(seconds=10)))
# print(add.apply_async(countdown = 120 , expires = datetime.datetime.now() + datetime.timedelta(days=9,hours =1)))
#
#
# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
#
#

#
# @periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
# def some_task(a,b):
#     return a+b
#
# print(some_task(2,9))
#
