from django.db import models

# Create your models here.
class Person(models.Model):
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    email=models.EmailField()
    period =models.DateField()
    month=models.IntegerField()

    def __str__(self):
        return self.receiver
