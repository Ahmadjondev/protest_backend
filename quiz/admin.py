from django.contrib import admin

from quiz.models import Science, Subject, Quiz, Section


# Register your models here.

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(Section)
class ScienceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',

    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'subject',
        'section',
    ]


@admin.register(Quiz)
class SubjectQuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'subject_id',
        'question_name',
        'var_a_name',
        'var_b_name',
        'var_c_name',
        'var_d_name',
        'correct',
    ]
