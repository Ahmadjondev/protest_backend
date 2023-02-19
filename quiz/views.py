from builtins import print

from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView

from user.models import User
from user.serializers import UserSerializer
from .serializer import QuizSerializer, SubjectSerializer, ScienceSerializer

from quiz.models import Science, Subject, Quiz


# Create your views here.

def user_detail(id: int):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user).data
    json: dict = {
        'id': serializer['id'],
        'name': serializer['name']

    }
    return json


def quiz_returned(serializer):
    json = serializer
    quiz_json: dict = {
        'id': json['id'],
        'science': json['science_id'],
        'subject': json['subject_id'],
        'akam_id': json['akam_id'],
        'question_name': json['question_name'],
        'var_a_name': json['var_a_name'],
        'var_a_id': json['var_a_id'],
        'var_b_name': json['var_b_name'],
        'var_b_id': json['var_b_id'],
        'var_c_name': json['var_c_name'],
        'var_c_id': json['var_c_id'],
        'var_d_name': json['var_d_name'],
        'var_d_id': json['var_d_id'],
        'correct': json['correct'],
        'owner': dict(user_detail(json['owner'])),
    }
    return quiz_json


class QuizView(APIView):

    # def post(self, request):
    #     data = request.data
    #     if data['action'] == 'create_quiz':
    #         # try:
    #         serializer = QuizSerializer(data=data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response({'ok': True, 'data': serializer.data})
    #     # except:
    #     #     return Response({'ok': False})

    def get(self, request):
        subject_id = request.query_params.get('subject')
        science_id = request.query_params.get('science')
        limit = request.query_params.get('limit')
        owner_id = request.query_params.get('science')
        if subject_id is not None:
            data_quiz = Quiz.objects.filter(subject=subject_id).values()
            serializer = QuizSerializer(data_quiz)
            print(data_quiz)
            list = []
            for data in data_quiz:
                list.append(quiz_returned(data))
            return Response({'ok': True, 'quizzes': list})
        if science_id is not None:
            data_quiz = Quiz.objects.filter(science=science_id).values()
            serializer = QuizSerializer(data_quiz)
            print(data_quiz)
            list = []
            for data in data_quiz:
                list.append(quiz_returned(data))
            return Response({'ok': True, 'quizzes': list})

    def science_json(id: int):
        science = Science.objects.get(id=id)
        serializer = ScienceSerializer(science)
        return serializer.data

    def subject_json(id: int):
        science = Subject.objects.get(id=id)
        serializer = SubjectSerializer(science)
        return serializer.data


class SubjectView(ListCreateAPIView):
    # queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # lookup_field = 'id'
    # def post(self, request):
    #     data = request.data
    #     if data['action'] == 'create_subject':
    #         try:
    #             serializer = SubjectSerializer(data=data)
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()
    #             return Response({'ok': True})
    #         except:
    #             return Response({'ok': False})
    #
    #     if data['action'] == 'delete_subject':
    #         try:
    #             subject = Subject.objects.get()
    #             subject.delete()
    #             return Response({'ok': True})
    #         except:
    #             return Response({'ok': False})
    #
    #     if data['action'] == 'subject':
    #         try:
    #             subject = Subject.objects.get()
    #             return Response({'ok': True, 'science': model_to_dict(subject)})
    #         except:
    #             return Response({'ok': False})

    # def get(self, request):
    #     # try:
    #     params = request.query_params['id']
    #     subjects = None
    #     if int(params) != 0:
    #         subjects = Subject.objects.filter(science=params).values()
    #     else:
    #         subjects = Subject.objects.all().values()
    #
    #     json: dict = SubjectSerializer(subjects).data
    #     lists: list = []
    #     for lesson in json:
    #         lists.append({
    #             'id': lesson['id'],
    #             'section_id': lesson['section_id'],
    #             'name': lesson['subject'],
    #             'science': lesson['science_id'],
    #         })
    #
    #     return Response({'ok': True, 'result': list})

    def get_queryset(self):
        id = self.request.query_params.get('id')
        if id is None:
            model_s = Subject.objects.all()
        else:
            model_s = Subject.objects.filter(science=id)
        return model_s


class ScienceView(ListAPIView):
    # Science Create, Delete, Read
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer

    def post(self, request):
        data = request.data
        if data['action'] == 'create_science':
            try:
                serializer = ScienceSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'ok': True})
            except:
                return Response({'ok': False})

        if data['action'] == 'delete_science':
            try:
                science = Science.objects.get()
                science.delete()
                return Response({'ok': True})
            except:
                return Response({'ok': False})

    # def get(self, request, **kwargs):
    #     # science_id = request.query_params.get('id')
    #     sciences = Science.objects.all().values()
    #     return Response({'ok': True, 'science': sciences})
