from django.contrib import admin

from histories.models import SubjectHistory


# Register your models here.


@admin.register(SubjectHistory)
class SubjectHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'results'
    ]
