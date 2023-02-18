from django.urls import path
from .views import RegisterUser, LoginUser, UserData, UserBadge

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login', LoginUser.as_view()),
    path('user', UserData.as_view()),
    path('badge', UserBadge.as_view()),
]
