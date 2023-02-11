from django.db import models


# Create your models here.

class Science(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Section(models.Model):
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}.{self.name}'


class Subject(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subjects', null=True)
    subject = models.TextField(verbose_name="Mavzu")
    science = models.IntegerField(null=True)

    def __str__(self):
        return self.subject


class Quiz(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['Subject-images', filename])

    science = models.IntegerField(blank=True, null=True)
    subject_id = models.IntegerField(blank=True, null=True)
    akam_id = models.IntegerField(null=True)
    question_name = models.TextField(verbose_name='Savol')
    question_image = models.ImageField(verbose_name='Subject Image:', upload_to=nameFile, blank=True, null=True)
    var_a_name = models.CharField(verbose_name='A:', max_length=555)
    var_a_id = models.IntegerField()
    var_b_name = models.CharField(verbose_name='B:', max_length=555)
    var_b_id = models.IntegerField()
    var_c_name = models.CharField(verbose_name='C:', max_length=555, blank=True)
    var_c_id = models.IntegerField(blank=True)
    var_d_name = models.CharField(verbose_name='D:', max_length=555, blank=True)
    var_d_id = models.IntegerField(blank=True)
    correct = models.IntegerField()
    owner = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.question_name
