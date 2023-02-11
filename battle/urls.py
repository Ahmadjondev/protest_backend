from rest_framework.urls import path

from battle.views import OneToOneBattle

urlpatterns = [
    path('one-to-one', OneToOneBattle.as_view())
]
