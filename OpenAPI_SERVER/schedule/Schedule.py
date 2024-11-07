from django.db import models

class Schedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventDate = models.DateTimeField()
    eventName = models.CharField(max_length=100)

