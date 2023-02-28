from rest_framework.urls import path

from quiz.views import ScienceView, SubjectView, QuizView

urlpatterns = [
    path('sciences', ScienceView.as_view()),
    path('subjects', SubjectView.as_view()),
    path('quizzes', QuizView.as_view()),
    path('solved', SolvedViewSet.as_view()),
]
