from django.forms import model_to_dict
from rest_framework import serializers
from .models import Science, Subject, Quiz, Section


class QuizSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subject_id = serializers.IntegerField(allow_null=True)
    question_name = serializers.CharField(max_length=1000)
    question_image = serializers.ImageField(allow_null=True)
    var_a_name = serializers.CharField(max_length=555)
    var_a_id = serializers.IntegerField()
    var_b_name = serializers.CharField(max_length=555)
    var_b_id = serializers.IntegerField()
    var_c_name = serializers.CharField(max_length=555, allow_blank=True)
    var_c_id = serializers.IntegerField(allow_null=True)
    var_d_name = serializers.CharField(max_length=555, allow_blank=True)
    var_d_id = serializers.IntegerField(allow_null=True)
    correct = serializers.IntegerField()
    owner = serializers.IntegerField(allow_null=True)

    def update(self, instance, validated_data):
        instance.subject_id = validated_data.get("subject_id")
        instance.question_name = validated_data.get("question_name")
        instance.question_image = validated_data.get("question_image")
        instance.var_a_name = validated_data.get("var_a_name")
        instance.var_a_id = validated_data.get("var_a_id")
        instance.var_b_name = validated_data.get("var_b_name")
        instance.var_b_id = validated_data.get("var_b_id")
        instance.var_c_name = validated_data.get("var_c_name")
        instance.var_c_id = validated_data.get("var_c_id")
        instance.var_d_name = validated_data.get("var_d_name")
        instance.var_d_id = validated_data.get("var_d_id")
        instance.correct = validated_data.get("correct")
        instance.owner = validated_data.get("owner")
        instance.save()
        return instance

    def create(self, validated_data):
        return Quiz.objects.create(**validated_data)


class SubjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    science = serializers.IntegerField()
    subject = serializers.CharField(max_length=1000)

    class Meta:
        model = Subject
        fields = ('id', 'subject', 'science')

    def update(self, instance, validated_data):
        instance.science = validated_data.get("science", instance.science)
        instance.subject = validated_data.get("subject", instance.subject)
        instance.save()
        return instance

    def create(self, validated_data):
        return Subject.objects.create(**validated_data)


class SectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=55)
    subjects = serializers.StringRelatedField(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.section = validated_data.get("section")
        instance.save()
        return instance

    def create(self, validated_data):
        return Science.objects.create(**validated_data)

    class Meta:
        model = Section
        fields = ('id', 'name', 'subjects')


class ScienceSerializer(serializers.ModelSerializer):
    sections = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Science
        fields = ('id', 'name', 'sections')
# id = serializers.IntegerField(read_only=True)
# name = serializers.CharField(max_length=55)
# section = serializers.CharField(max_length=55)
#
# def update(self, instance, validated_data):
#     instance.name = validated_data.get("name")
#     instance.section = validated_data.get("section")
#     instance.save()
#     return instance
#
# def create(self, validated_data):
#     return Science.objects.create(**validated_data)
