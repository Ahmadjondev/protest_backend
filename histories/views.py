from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView

from histories.models import SubjectHistory
from histories.serializers import SubjectHistorySerializer


# Create your views here.

class CreateSubjectHistoriesView(ListCreateAPIView):
    serializer_class = SubjectHistorySerializer
    queryset = SubjectHistory.objects.all()
