import os

from django.db import models

from quiz.models import Quiz, Science
from user.models import User


# Create your models here.

class ContestQuiz(models.Model):
    name = models.ForeignKey(Science, on_delete=models.DO_NOTHING)
    questions = models.ManyToManyField(Quiz, blank=True)

    def __str__(self):
        return f"{self.name}"


class Contest(models.Model):
    def imageName(self, filename):
        return "/".join(["ContestImages", filename])

    name = models.CharField(max_length=150)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to=imageName, blank=True, null=True)
    price = models.CharField(max_length=10, default=0)  # join contest price => 1000
    powered_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    started_at = models.DateTimeField()
    time = models.IntegerField(default=360)
    contest_type = models.IntegerField(default=0)
    code = models.CharField(max_length=6, null=True, blank=True)
    ball = models.DecimalField(decimal_places=2, max_digits=3)
    position_1 = models.IntegerField(default=0, null=True, blank=True)
    position_2 = models.IntegerField(default=0, null=True, blank=True)
    position_3 = models.IntegerField(default=0, null=True, blank=True)
    questions = models.ManyToManyField(ContestQuiz, blank=True)


class ContestUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    time = models.IntegerField()
    ball = models.DecimalField(max_digits=5, decimal_places=2)
    participation = models.BooleanField(default=False)
