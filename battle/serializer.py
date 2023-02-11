from rest_framework import serializers

from battle.models import OneToOne


class OneToOneSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_1 = serializers.IntegerField()
    user_2 = serializers.IntegerField(allow_null=True)
    quiz_count = serializers.IntegerField()
    science = serializers.CharField(max_length=33)
    winner = serializers.CharField(max_length=55, default='', allow_blank=True)
    correct_1 = serializers.IntegerField(default=0)
    correct_2 = serializers.IntegerField(default=0)
    # time = serializers.IntegerField(default=300)
    code = serializers.CharField(max_length=6)
    current_question_1 = serializers.IntegerField(default=0)
    current_question_2 = serializers.IntegerField(default=0)
    is_finished = serializers.BooleanField(default=False)
    is_started = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        instance.user_1 = validated_data.get("user_1")
        instance.user_2 = validated_data.get("user_2")
        instance.quiz_count = validated_data.get("quiz_count")
        instance.science = validated_data.get("science")
        instance.winner = validated_data.get("winner")
        instance.correct_1 = validated_data.get("correct_1")
        instance.correct_2 = validated_data.get("correct_2")
        # instance.time = validated_data.get("time", instance.time)
        instance.code = validated_data.get("code")
        instance.current_question_1 = validated_data.get("current_question_1")
        instance.current_question_2 = validated_data.get("current_question_2")
        instance.is_finished = validated_data.get("is_finished")
        instance.is_started = validated_data.get("is_started")
        instance.save()
        return instance

    def create(self, validated_data):
        return OneToOne.objects.create(**validated_data)
