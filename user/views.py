from django.forms import model_to_dict
from rest_framework.generics import ListAPIView

from .models import User, Badge
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
import os


# Create your views here.
class RegisterUser(APIView):

    def post(self, request):
        data = request.data

        if data['action'] == 'check_phone':
            try:
                User.objects.get(phone=data['phone'])
                return Response({'ok': True})
            except:
                return Response({'ok': False})

        # SMS Verify
        if data['action'] == 'phone_verify':
            pass

        if data['action'] == 'create_user':
            # try:
                serializer = UserSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(
                    {'ok': True, 'id': serializer.data['id'], 'message': "Foydanunchi muvaffaqiyatli yaratildi"})
            # except:
                return Response({'ok': False, 'error': 'User yaratilmadi'})


class LoginUser(APIView):
    def post(self, request):
        data = request.data
        if data['action'] == 'login':
            try:
                user = User.objects.get(phone=data['phone'], password=data['password'])
                serializer = UserSerializer(user)
                return Response({'ok': True, 'id': serializer.data['id']})
            except:
                return Response({'ok': False})


class UserData(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data

        if data['action'] == 'get_user':
            user = User.objects.get(id=int(data['id']))
            serializer = UserSerializer(user)
            return Response(serializer.data)
        # Muammo bor
        if data['action'] == 'update_coins':
            user = User.objects.get(id=data['id'])
            json = model_to_dict(user)
            json['coins'] += int(data['coins'])
            serializer = UserSerializer(instance=user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'message': "Tanga qoshildi"})
        # Muammo bor
        if data['action'] == 'update_ball':
            user = User.objects.get(id=data['id'])
            json = model_to_dict(user)
            json['ball'] += (data['ball'])
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'message': "Ball yangilandi"})

        # Muammo bor
        if data['action'] == 'change_image':
            user = User.objects.get(id=data['id'])
            json = model_to_dict(user)
            file = f"assets/{json['image']}"
            json['image'] = data['image']
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            if os.path.isfile(file):
                os.remove(file)
            return Response({'ok': True})

        if data['action'] == 'follow':
            user = User.objects.get(id=data['user'])
            to_user = User.objects.get(id=data['to_user'])
            if to_user in list(user.following.all()):
                user.following.remove(to_user)
                user.save()
                to_user.followers.remove(user)
                to_user.save()
                return Response({'ok': True})
            else:
                user.following.add(to_user)
                user.save()
                to_user.followers.add(user)
                to_user.save()
                return Response({'ok': True})


# 2 versiyada aktivlashadi
class UserBadge(APIView):
    def get(self, request):
        data = request.data
        try:
            user = User.objects.get(id=data['id'])
            serializer = UserSerializer(user)
        except User.DoesNotExist:
            user = None
        try:
            badge = Badge.objects.get(id=data['id'])
        except Badge.DoesNotExist:
            badge = None

        if user is not None and badge is not None:
            if user in badge.objects.all():
                print("This have a Badge")
            else:
                badge.add(user)
        a = UserSerializer(user)
        return Response({'ok': a.data})
