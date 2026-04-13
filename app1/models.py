from django.db import models

# Create your models here.
class students(models.Model):
    std_id=models.IntegerField(unique=True)
    std_name=models.CharField(max_length=25)
    std_dept=models.CharField(max_length=15)


class deparments(models.Model):
    dept_name=models.CharField(max_length=30)
    dept_head=models.CharField(max_length=10)


class faculty(models.Model):
    faculty_id=models.IntegerField(unique=True)
    faculty_name=models.CharField(max_length=15)
