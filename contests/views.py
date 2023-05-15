from django.forms import model_to_dict
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from contests.models import Contest, ContestQuiz, ContestUser
from contests.serializers import ContestSerializer, CreateContestSerializer, ContestQuizSerializer, \
    ContestUserSerializer
from user.models import User


# Create your views here.

class ContestListView(ListAPIView):  # Get All Contest
    serializer_class = ContestSerializer

    queryset = Contest.objects.all()


class ContestView(RetrieveAPIView):  # View a Contest
    serializer_class = ContestSerializer
    queryset = Contest.objects.all()


class CreateContest(CreateAPIView):  # Create Contest
    serializer_class = CreateContestSerializer


class CreateQuizContest(CreateAPIView):  # Create Contest Questions
    serializer_class = ContestQuizSerializer


class ListQuizContest(ListAPIView):  # Get a contest questions
    serializer_class = ContestQuizSerializer

    def get_queryset(self):
        params = self.request.query_params.get('id')
        return ContestQuiz.objects.filter(contest=params)


class CreateContestUserView(CreateAPIView):
    serializer_class = ContestUserSerializer
    queryset = ContestUser

    def perform_create(self, serializer):
        print(self.request.data)
        # user = User.objects.get(id=)
        # user_json = model_to_dict(user)
        # contest = Contest.objects.get(id=contest_id)
        # contest_json = model_to_dict(contest)
        # if int(user_json['balance']) >= int(contest_json['price']):
        #     user_json['balance'] -= int(contest_json['price'])
        #
        # else:
        #     return Response({'ok': False, 'message': "Hisobingizda mablag' yetarli emas"})
        # serializer.save()


class ContestUserView(APIView):

    def post(self, request):
        user_id = self.request.query_params.get('id')
        contest_id = self.request.query_params.get('contest')
        data = self.request.data
        if data['action'] == 'join':
            user = User.objects.get(id=user_id)
            user_json = model_to_dict(user)
            contest = Contest.objects.get(id=contest_id)
            contest_json = model_to_dict(contest)
            if int(user_json['balance']) >= int(contest_json['price']):
                user_json['balance'] -= int(contest_json['price'])

            else:
                return Response({'ok': False, 'message': "Hisobingizda mablag' yetarli emas"})
        if data['action'] == 'update':
            user = ContestUser.objects.get(user=user_id, contest=contest_id)
            contest_user = dict(model_to_dict(user))
            contest_user['time'] = data['time']
            contest_user['ball'] = data['ball']
            contest_user['participation'] = data['participation']
            serializer = ContestUserSerializer(user, data=contest_user)
            serializer.is_valid()
            serializer.save()
            json = dict(serializer.data)
            return Response(json)
        return Response(False)

    def get(self, request):
        user_id = self.request.query_params.get('id')
        contest_id = self.request.query_params.get('contest')
        user = ContestUser.objects.get(user=user_id, contest=contest_id)
        serializer = ContestUserSerializer(user)
        json = dict(serializer.data)
        # if not json['participation']:
        #     return Response(False)
        return Response(dict(serializer.data))
