from django.contrib import admin

from battle.models import OneToOne


# Register your models here.

@admin.register(OneToOne)
class BattleAdmin(admin.ModelAdmin):
    list_display = ['user_1', 'user_2', 'science', 'quiz_count']
