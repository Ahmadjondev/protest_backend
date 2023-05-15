from rest_framework.urls import path

from histories.views import HistoriesView, CreateHistoryView

urlpatterns = [
    path('history', HistoriesView.as_view()),
    path('history/create', CreateHistoryView.as_view())
]
