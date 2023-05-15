from django.urls import path
from .views import RegisterUser, LoginUser, UserData, UserBadge, LeaderBoard

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login', LoginUser.as_view()),
    path('user', UserData.as_view()),
    path('badge', UserBadge.as_view()),
    path('leaderboard', LeaderBoard.as_view()),
]
