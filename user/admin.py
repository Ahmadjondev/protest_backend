from django.contrib import admin
from .models import User,Badge


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'surname',
        'username',
        'phone',
        'region',
        'city',
        'ball',
        'coins',
        'created_at',
        'is_online'
    ]
    search_fields = [
        'id',
        'name',
        'surname',
        'username',
        'phone',
        'region',
        'city',
        'ball',
        'coins',
        'created_at',
        'is_online'
    ]


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'name',
        'desc',
        # 'badge_id',
    ]

