from django.forms import model_to_dict
from rest_framework import serializers
from .models import Science, Subject, Quiz, Section


class QuizSerializer(serializers.Serializer):
    # model = Quiz
    # fields = ['id', 'science', 'subject', 'question_name', 'question_image', 'var_a_name', 'var_a_id', 'var_b_name',
    #           'var_b_id', 'var_c_name', 'var_c_id', 'var_d_name', 'var_d_id', 'correct', 'owner']

    id = serializers.IntegerField(read_only=True)
    subject = serializers.IntegerField(allow_null=True)
    science = serializers.IntegerField(allow_null=True)
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
        instance.subject_id = validated_data.get("subject")
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
    question_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Subject
        fields = ('id', 'subject', 'section', 'science', 'question_count')

    def get_question_count(self, obj):
        quiz = Quiz.objects.filter(subject=obj.id).count()
        return quiz


class SectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=55)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.save()
        return instance

    def create(self, validated_data):
        return Science.objects.create(**validated_data)

    class Meta:
        model = Section
        fields = ('id', 'name')


class ScienceSerializer(serializers.ModelSerializer):
    section = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Science
        fields = ['id', 'name', 'section']

    def get_section(self, obj):
        s = Section.objects.filter(science=obj.id).values()
        return s

        # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=55)
    # section = serializers.StringRelatedField()
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name")
    #     instance.section = validated_data.get("section")
    #     instance.save()
    #     return instance
    #
    # def create(self, validated_data):
    #     return Science.objects.create(**validated_data)
