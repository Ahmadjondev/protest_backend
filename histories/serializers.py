from rest_framework import serializers

from histories.models import QuizHistory
from quiz.models import Quiz, Science
from quiz.serializer import QuizSerializer, ScienceSerializer


class CreateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizHistory
        fields = ['user', 'type', 'time', 'ball', 'test_count', 'ended_time', 'result']


class HistorySerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    class Meta:
        model = QuizHistory
        fields = ['user', 'type', 'time', 'ball', 'test_count', 'ended_time', 'result']

    def get_result(self, obj):
        result = []

        try:
            r = list(obj.result)
            for item in r:
                result2 = []
                count = 0
                unchecked = 0
                for item2 in item['questions']:
                    quiz_model = Quiz.objects.get(id=int(item2['quiz_id']))
                    quiz = dict(QuizSerializer(quiz_model).data)
                    quiz.pop('akam_id')
                    quiz['checked'] = item2['checked']
                    if quiz['checked'] == quiz['correct']:
                        count += 1
                    if quiz['checked'] == 0:
                        unchecked += 1
                    result2.append(quiz)
                science = Science.objects.get(id=item['science'])
                science_serializer = ScienceSerializer(science).data
                res = {
                    "name": science_serializer['name'],
                    "question_count": len(result2),
                    "correct_count": count,
                    "unchecked": unchecked,
                    'questions': result2
                }
                result.append(res)
        except:
            pass

        return result
