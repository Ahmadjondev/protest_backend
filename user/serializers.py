from rest_framework import serializers
from .models import User, Badge


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'name', 'desc', 'user']


class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'image', 'ball']


class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField(read_only=True)
    following_count = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(allow_null=True)
    badge = BadgeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'image', 'phone', 'birthday', 'region', 'city', 'ball', 'coins',
                  'created_at', 'badge', 'followers_count', 'following_count']


    def get_following_count(self, obj):
        count = obj.following.all().count()
        return count

    def get_followers_count(self, obj):
        count = obj.followers.all().count()
        return count
