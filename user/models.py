from django.db import models


# Create your models here.


class Badge(models.Model):
    icon = models.ImageField(upload_to='User-badges/', blank=False, null=True)
    name = models.CharField(max_length=30)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['User-images', str(instance.username), filename])

    username = models.CharField(max_length=30)
    image = models.ImageField(verbose_name='Image:', upload_to=nameFile, blank=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, blank=True)
    mail = models.CharField(blank=True, max_length=55)
    password = models.CharField(max_length=30)
    birthday = models.CharField(max_length=10)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    ball = models.DecimalField(max_digits=16, decimal_places=0, default=0)
    coins = models.DecimalField(max_digits=16, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=True)
    badge = models.ManyToManyField(Badge, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
