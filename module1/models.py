from django.db import models
class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    class Meta:
        db_table ="register"
# Create your models here.
class Feedback(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email = models.EmailField(primary_key=True)
    Comment=models.CharField(max_length=100000)

    class Meta:
        db_table="Feedback"