from celery import shared_task
from time import sleep
from django.http import HttpResponse



@shared_task
def sleepy(duration):
    sleep(duration)
    return HttpResponse("<h1>Hello, Its an Celery</h1>")

