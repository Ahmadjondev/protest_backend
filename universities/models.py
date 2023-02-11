from django.db import models


# Create your models here.

class University(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=800, blank=True)
    image = models.CharField(max_length=300, blank=True)
    map = models.CharField(max_length=800, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=800, blank=True)
    profession = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name


class Study(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    study_name = models.CharField(max_length=400)
    university_id = models.ForeignKey(University, on_delete=models.DO_NOTHING)
    science_1 = models.CharField(max_length=55)
    science_2 = models.CharField(max_length=55)
    grant_ball = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    contract_ball = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    grant_count = models.IntegerField(default=0, blank=True)
    contract_count = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.study_name
