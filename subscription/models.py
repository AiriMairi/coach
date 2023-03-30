from django.db import models
from user.models import User


class Subscription(models.Model):
    PLAN_CHOICES = (
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('ultimate', 'Ultimate'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=10, choices=PLAN_CHOICES)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
