from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    max_capacity = models.PositiveIntegerField()
    current_capacity = models.PositiveIntegerField(default=0)
