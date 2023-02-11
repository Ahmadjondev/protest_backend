from django.db import models


# Create your models here.

class OneToOne(models.Model):
    user_1 = models.IntegerField(default=0)
    user_2 = models.IntegerField(blank=True, null=True)
    quiz_count = models.IntegerField()
    science = models.CharField(max_length=33)
    winner = models.CharField(max_length=55, default='')
    correct_1 = models.IntegerField(default=0)
    correct_2 = models.IntegerField(default=0)
    code = models.CharField(max_length=6)
    current_question_1 = models.IntegerField(default=0)
    current_question_2 = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    is_started = models.BooleanField(default=False)

# class OneToOneHistory(models.Model):
#     user_1 = models.CharField(max_length=55)
#     user_2 = models.CharField(max_length=55, blank=True)
#     # user_1_id = models.IntegerField(verbose_name="User 1")
#     # user_2_id = models.IntegerField(verbose_name="User 2")
#     quiz_count = models.IntegerField()
#     science = models.CharField(max_length=33)
#     winner = models.CharField(max_length=55, default='')
#     correct_1 = models.IntegerField(default=0)
#     correct_2 = models.IntegerField(default=0)
#     code = models.CharField(max_length=6)
#     current_question_1 = models.IntegerField(default=0)
#     current_question_2 = models.IntegerField(default=0)
#     is_finished = models.BooleanField(default=False)
#     is_started = models.BooleanField(default=False)
