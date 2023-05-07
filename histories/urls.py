from rest_framework.urls import path

from histories.views import CreateSubjectHistoriesView

urlpatterns = [
    path('history/create-subject', CreateSubjectHistoriesView.as_view())
]
