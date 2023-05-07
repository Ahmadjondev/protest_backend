from django.forms import model_to_dict
from rest_framework import serializers

from histories.models import SubjectHistory
from quiz.models import Quiz
from quiz.serializer import QuizSerializer


class SubjectHistorySerializer(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = SubjectHistory
        fields = ('user', 'subject', 'science', 'ball', 'test_count', 'ended_time', 'results')

    def get_results(self, obj):
        r = list(obj.results)
        result = []
        for item in r:
            print(item['quiz_id'])
            quizModel = Quiz.objects.get(id=item['quiz_id'])
            quiz = dict(QuizSerializer(quizModel).data)
            quiz.pop('akam_id')
            quiz['checked'] = item['checked']
            result.append(quiz)
        return result
