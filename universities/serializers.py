from rest_framework import serializers
from universities.models import University


class UniversitiesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=400)
    description = serializers.CharField(max_length=800, allow_blank=True)
    image = serializers.CharField(max_length=300, allow_blank=True)
    map = serializers.CharField(max_length=800, allow_blank=True)
    phone = serializers.CharField(max_length=20, allow_blank=True)
    address = serializers.CharField(max_length=255, allow_blank=True)
    keywords = serializers.CharField(max_length=800, allow_blank=True)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id")
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.image = validated_data.get("image")
        instance.map = validated_data.get("map")
        instance.phone = validated_data.get("phone")
        instance.address = validated_data.get("address")
        instance.keywords = validated_data.get("keywords")
        instance.save()
        return instance

    def create(self, validated_data):
        return University.objects.create(**validated_data)
