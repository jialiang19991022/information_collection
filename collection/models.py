from django.db import models

# Create your models here.

class information(models.Model):
    stu_number = models.CharField(max_length=8, unique=True)
    sex = models.CharField(max_length=5)
    major = models.CharField(max_length=4)
    name = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=11)
    first_department = models.CharField(max_length=4)
    second_department = models.CharField(max_length=4)
    notes = models.TextField(max_length=800)
    experiences = models.TextField(max_length=800)
    wishes = models.TextField(max_length=800)
    QQ_number = models.CharField(max_length=13)
    img = models.CharField(max_length=10000)
