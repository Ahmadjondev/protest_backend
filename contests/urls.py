from rest_framework.urls import path

from contests.views import ContestListView, CreateQuizContest, CreateContest, ListQuizContest, ContestView, \
    ContestUserView, CreateContestUserView

urlpatterns = [
    path('contests', ContestListView.as_view()),  # All Contest view
    path('contests/<int:pk>', ContestView.as_view()),  # A Contest view
    path('contests/create', CreateContest.as_view()),  # Create Contest
    path('contests/questions', ListQuizContest.as_view()),  # A Contest Questions
    path('contests/questions/create', CreateQuizContest.as_view()),  # A Contest Questions create
    path('contests/leaderboard', ContestListView.as_view()),  # A Contest Leaderboard
    path('contests/user', ContestUserView.as_view()),  # A Contest User Ball or participation update
    path('contests/user/create', CreateContestUserView.as_view()),  # A Contest User Ball or participation update
    # path('contests/user/<int:pk>', ContestListView.as_view())  # A Get Contest User
]
