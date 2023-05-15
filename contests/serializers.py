from rest_framework import serializers

from contests.models import Contest, ContestQuiz, ContestUser
from quiz.serializer import ScienceSerializer
from user.serializers import UserSerializer


class ContestQuizSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()

    class Meta:
        model = ContestQuiz
        fields = ('name', 'questions')

    def get_questions(self, obj):
        return obj.questions.all().values()

    def get_name(self, obj):
        serializer = ScienceSerializer(obj.name)
        return serializer.data['name']


class CreateContestQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestQuiz
        fields = ['name', 'questions']


class ContestSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    # questions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Contest
        fields = (
            'id', 'name', 'author', 'desc', 'price', 'started_at', 'time', 'contest_type', 'code', 'ball', 'position_1',
            'position_2', 'position_3',)

    def get_author(self, obj):
        serializer = UserSerializer(obj.powered_by).data
        return serializer['name']

    # def get_questions(self, obj):
    #     ques = obj.questions.all().values()
    #     return ques


class CreateContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'


class ContestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestUser
        fields = ('user', 'contest', 'time', 'ball', 'participation')
