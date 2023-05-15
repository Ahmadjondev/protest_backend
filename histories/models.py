from datetime import datetime, timedelta

from django.db import models

from quiz.models import Subject, Science
from user.models import User


# Create your models here.
class QuizHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)  # mavzuli , fanli , dtm , virtual , // SAT , IELTS
    ball = models.DecimalField(decimal_places=2, max_digits=5)
    test_count = models.IntegerField()
    time = models.IntegerField(null=True, blank=True)
    ended_time = models.DateTimeField(auto_now=True)
    result = models.JSONField(name='result')

    @classmethod
    def last_week_result(cls):
        last_week = datetime.now() - timedelta(days=7)
        return cls.objects.filter(ended_time__gte=last_week)
