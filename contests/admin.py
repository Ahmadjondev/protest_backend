from django.contrib import admin

from contests.models import Contest


# Register your models here.

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
