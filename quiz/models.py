from django.db import models
from django.contrib.auth.models import User


class Science(models.Model):

    def scienceImage(filename):
        return '/'.join(['Science-images', filename])

    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to=scienceImage, null=True, blank=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name='section')
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subject(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section', null=True)
    subject = models.TextField(verbose_name="Mavzu")
    science = models.ForeignKey(Science, on_delete=models.CASCADE, blank=True, related_name='science', null=True)

    def __str__(self):
        return self.subject


class Quiz(models.Model):

    def nameFile(self, filename):
        return '/'.join(['SubjectImages', filename])

    def answerFile(self, filename):
        return '/'.join(['AnswerImages', filename])

    science = models.ForeignKey(Science, blank=True, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)

    akam_id = models.IntegerField(null=True)

    question_name = models.TextField(verbose_name='Savol', blank=True)
    question_image = models.ImageField(verbose_name='Rasmli savol:', upload_to=nameFile, blank=True, null=True)

    var_a_name = models.CharField(verbose_name='A:', max_length=555, null=True, blank=True)
    var_a_image = models.ImageField(upload_to=answerFile, null=True, blank=True)
    var_a_id = models.IntegerField()

    var_b_name = models.CharField(verbose_name='B:', max_length=555, null=True, blank=True)
    var_b_image = models.ImageField(upload_to=answerFile, null=True, blank=True)
    var_b_id = models.IntegerField()

    var_c_name = models.CharField(verbose_name='C:', max_length=555, null=True, blank=True)
    var_c_image = models.ImageField(upload_to=answerFile, null=True, blank=True)
    var_c_id = models.IntegerField(blank=True)

    var_d_name = models.CharField(verbose_name='D:', max_length=555, null=True, blank=True)
    var_d_image = models.ImageField(upload_to=answerFile, null=True, blank=True)
    var_d_id = models.IntegerField(blank=True)

    correct = models.IntegerField()

    owner = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.question_name

    @staticmethod
    def quiz_count(index: int):
        return Quiz.objects.filter(subject_id=index).count()


class Solved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    science = models.ForeignKey(Science, blank=True, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE)
    answers = models.TextField()
    result = models.CharField(max_length=555, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
