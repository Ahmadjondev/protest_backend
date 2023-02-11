from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()
    username = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    # profession = serializers.CharField(max_length=15, allow_blank=True)
    birthday = serializers.CharField(max_length=10)
    region = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    ball = serializers.IntegerField()
    coins = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    is_online = serializers.BooleanField(default=False)

    def update(self, instance, validated_data):
        instance.image = validated_data.get("image")
        instance.username = validated_data.get("username")
        instance.name = validated_data.get("name")
        instance.surname = validated_data.get("surname")
        instance.phone = validated_data.get("phone")
        instance.birthday = validated_data.get("birthday")
        instance.password = validated_data.get("password")
        # instance.profession = validated_data.get("profession", instance.profession)
        instance.region = validated_data.get("region")
        instance.city = validated_data.get("city")
        instance.ball = validated_data.get("ball")
        instance.coins = validated_data.get("coins")
        instance.created_at = validated_data.get("created_at")
        instance.is_online = validated_data.get("is_online")
        instance.save()
        return instance

    def create(self, validated_data):
        return User.objects.create(**validated_data)
