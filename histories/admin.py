from django.contrib import admin

from histories.models import QuizHistory


# Register your models here.


@admin.register(QuizHistory)
class SubjectHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        # 'results'
    ]
