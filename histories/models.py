from django.db import models

from quiz.models import Subject, Science
from user.models import User


# Create your models here.
class SubjectHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    ball = models.DecimalField(decimal_places=2, max_digits=5)
    test_count = models.IntegerField()
    ended_time = models.DateTimeField(auto_now=True)
    result = models.JSONField(blank=True, null=True, name='results')
