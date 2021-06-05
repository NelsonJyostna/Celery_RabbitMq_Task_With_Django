from django.db import models
import sqlalchemy as sa


# Create your models here.
class Student(models.Model):
     id=models.AutoField(primary_key=True)
     status=models.CharField(max_length=20)
     item=models.CharField(max_length=20)
