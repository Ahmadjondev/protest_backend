from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView

from histories.models import QuizHistory
from histories.serializers import HistorySerializer, CreateHistorySerializer
from user.serializers import MiniUserSerializer


# Create your views here.

class HistoriesView(ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', 0)
        return QuizHistory.objects.filter(user_id=id).order_by('-ended_time')


class ActiveUserView(ListAPIView):
    serializer_class = MiniUserSerializer

    def get_queryset(self):
        QuizHistory.last_week_result()


class CreateHistoryView(CreateAPIView):
    serializer_class = CreateHistorySerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({'ok': True})
