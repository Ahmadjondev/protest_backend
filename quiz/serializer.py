from rest_framework import serializers

from user.models import User
from user.serializers import UserSerializer
from .models import Science, Subject, Quiz, Section


def get_owner(obj):
    user = User.objects.get(id=obj.owner)
    serializer = UserSerializer(user)
    return serializer.data


class QuizSerializer(serializers.ModelSerializer):
    # owner = serializers.SerializerMethodField(read_only=True)
    # science = serializers.SerializerMethodField(read_only=True)
    # subject = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = (
            'id', 'akam_id', 'question_name', 'question_image', 'var_a_name', 'var_a_image',
            'var_a_id', 'var_b_name', 'var_b_image', 'var_b_id', 'var_c_name', 'var_c_image', 'var_c_id', 'var_d_name',
            'var_d_image', 'var_d_id', 'correct')

    def get_science(self, obj):
        science = Science.objects.get(id=obj.id)
        serializer = ScienceSerializer(science)
        return {'name': serializer.data['name'], 'id': serializer.data['id']}

    def get_subject(self, obj):
        science = Subject.objects.get(id=obj.id)
        serializer = SubjectSerializer(science)
        return {'name': serializer.data['subject'], 'id': serializer.data['id']}


class SubjectSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField(read_only=True)
    sections = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Subject
        fields = ('id', 'subject', 'sections', 'question_count')

    def get_question_count(self, obj):
        quiz = Quiz.objects.filter(subject=obj.id).count()
        return quiz

    def get_sections(self, obj):
        section = Section.objects.get(id=obj.section_id)
        serializer = SectionSerializer(section)
        return serializer.data


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'science')


class ScienceSerializer(serializers.ModelSerializer):
    section = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Science
        fields = ['id', 'name', 'section']

    def get_section(self, obj):
        sections = list(Section.objects.filter(science=obj.id).values())
        return sections
