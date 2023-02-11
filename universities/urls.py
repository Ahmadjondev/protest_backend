from rest_framework.urls import path
from universities.views import UniversitiesData

urlpatterns = [
    path('universities', UniversitiesData.as_view())
]
