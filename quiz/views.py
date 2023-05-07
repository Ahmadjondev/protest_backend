from rest_framework import generics

from quiz.models import Science, Subject, Quiz, Section
from user.models import User
from user.serializers import UserSerializer
from .serializer import SubjectSerializer, ScienceSerializer, QuizSerializer


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


class QuizView(generics.ListCreateAPIView):
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        data = self.request.data
        print(data)
        try:
            Quiz.objects.get(akam_id=data['akam_id'])
        except Quiz.DoesNotExist:
            subject = Subject.objects.get(id=data['subject'])
            science = Science.objects.get(id=data['science'])
            serializer.save(subject=subject, science=science)

    def get_queryset(self):
        subject_id = self.request.query_params.get('subject')
        science_id = self.request.query_params.get('science')
        limit = self.request.query_params.get('limit')

        # versiya 2 da userlar test qoshishi mumkin
        # owner_id = request.query_params.get('science')

        if subject_id is not None:
            return Quiz.objects.filter(subject=int(subject_id)).order_by('?')

        if science_id is not None and limit is not None:
            return Quiz.objects.filter(science=int(science_id)).order_by('?')[:int(limit)]


class SubjectView(generics.ListCreateAPIView):
    # queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def perform_create(self, serializer):
        data = self.request.data
        section = Section.objects.get(id=data['section'])
        science = Science.objects.get(id=data['science'])
        serializer.save(section=section, science=science)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        if id == 0 or id is None:
            model_s = Subject.objects.all()
        else:
            model_s = Subject.objects.filter(science=id)
        return model_s


class ScienceView(generics.ListCreateAPIView):
    # Science Create, Delete, Read
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer

    # def post(self, request):
    #     data = request.data
    #     if data['action'] == 'create_science':
    #         try:
    #             serializer = ScienceSerializer(data=data)
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()
    #             return Response({'ok': True})
    #         except:
    #             return Response({'ok': False})
    #
    #     if data['action'] == 'delete_science':
    #         try:
    #             science = Science.objects.get()
    #             science.delete()
    #             return Response({'ok': True})
    #         except:
    #             return Response({'ok': False})

    # def get(self, request, **kwargs):
    #     # science_id = request.query_params.get('id')
    #     sciences = Science.objects.all().values()
    #     return Response({'ok': True, 'science': sciences})
