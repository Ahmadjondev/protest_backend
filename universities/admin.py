from django.contrib import admin
from .models import University, Study


# Register your models here.
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'phone',
        'address'
    ]


@admin.register(Study)
class UniversityAdmin(admin.ModelAdmin):
    list_display = [
        'university_id',
        'study_name',
        'science_1',
        'science_2',
        'grant_ball',
        'contract_ball'
    ]
