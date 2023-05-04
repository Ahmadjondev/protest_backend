from django.contrib import admin
from .models import User,Badge


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'surname',
        'phone',
        'region',
        'city',
        'ball',
        'coins',
        'created_at'
    ]
    search_fields = [
        'id',
        'name',
        'surname',
        'phone',
        'region',
        'city',
        'ball',
        'coins',
        'created_at'
    ]


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'desc',
        # 'badge_id',
    ]

