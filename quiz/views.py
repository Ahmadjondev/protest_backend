from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .serializer import QuizSerializer, SubjectSerializer, ScienceSerializer

from quiz.models import Science, Subject, Quiz


# Create your views here.

class QuizView(APIView):
    def post(self, request):
        data = request.data
        if data['action'] == 'create_quiz':
            # try:
            serializer = QuizSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'data': serializer.data})
        # except:
        #     return Response({'ok': False})

    def get(self, request):
        data = request.query_params
        return Response({data})


class SubjectView(APIView):

    def post(self, request):
        data = request.data
        if data['action'] == 'create_subject':
            try:
                serializer = SubjectSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'ok': True})
            except:
                return Response({'ok': False})

        if data['action'] == 'delete_subject':
            try:
                subject = Subject.objects.get(id=data['id'])
                subject.delete()
                return Response({'ok': True})
            except:
                return Response({'ok': False})

        if data['action'] == 'subject':
            try:
                subject = Subject.objects.get()
                return Response({'ok': True, 'science': model_to_dict(subject)})
            except:
                return Response({'ok': False})

    def get(self, request):
        # try:
        params = request.query_params['id']
        subjects = None
        if int(params) != 0:
            subjects = Subject.objects.filter(science=params).values()
        else:
            subjects = Subject.objects.all().values()
        serializer = SubjectSerializer(subjects)
        return Response({'ok': True, 'result': subjects})
    # except:
    #     return Response({'ok': False, 'result': []})


class ScienceView(ListAPIView):
    # Science Create, Delete, Read
    serializer_class = ScienceSerializer
    queryset = Science.objects.all()

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

        if data['action'] == 'science':
            # try:
            science = Science.objects.get(id=data['id'])
            return Response({'ok': True, 'science': model_to_dict(science)})
        # except:
        #     return Response({'ok': False})
