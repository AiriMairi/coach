from django.db import models
from user.models import User


class CoachingSession(models.Model):
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_capacity = models.PositiveIntegerField()
    current_capacity = models.PositiveIntegerField(default=0)
