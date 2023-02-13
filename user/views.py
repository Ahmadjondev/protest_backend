from django.forms import model_to_dict

from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import UserSerializer
import os


# Create your views here.

class TemplateView(TemplateView):
    template_name = 'index.html'


class RegisterUser(APIView):

    def post(self, request):
        data = request.data
        if data['action'] == 'check_user':
            try:
                User.objects.get()
                return Response({'ok': True})
            except:
                return Response({'ok': False})

        if data['action'] == 'check_phone':
            try:
                User.objects.get()
                return Response({'ok': True})
            except:
                return Response({'ok': False})

        if data['action'] == 'create_user':
            # try:
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {'ok': True, 'id': serializer.data['id'], 'message': "Foydanunchi muvaffaqiyatli yaratildi"})
        # except:
        #     return Response({'ok': False, 'error': 'User yaratilmadi'})

        if data['action'] == 'check_ball':
            user = list(User.objects.filter(ball=15).values())
            return Response({'length': len(user)})


class LoginUser(APIView):
    def post(self, request):
        data = request.data
        if data['action'] == 'login':
            try:
                user = None
                if data['phone'] == '' or data['phone'] is None:
                    user = User.objects.get(username=data['username'], password=data['password'])
                else:
                    user = User.objects.get(phone=data['phone'], password=data['password'])
                serializer = UserSerializer(user)
                return Response({'ok': True, 'id': serializer.data['id']})
            except:
                return Response({'ok': False})


class UserData(APIView):
    def post(self, request):
        data = request.data
        if data['action'] == 'get_user':
            user = User.objects.get(id=data['id'])
            serializer = UserSerializer(user)
            return Response(serializer.data)

        if data['action'] == 'update_coins':
            user = User.objects.get(id=data['id'])
            json = model_to_dict(user)
            json['coins'] += int(data['coins'])
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'message': "Tanga qoshildi"})

        if data['action'] == 'update_ball':
            user = User.objects.get(id=data['id'])
            json = model_to_dict(user)
            json['ball'] += (data['ball'])
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'message': "Ball yangilandi"})

        if data['action'] == 'update_online':
            user = User.objects.get(id=data['id'])
            json = model_to_dict(user)
            json['is_online'] = bool(data['is_online'])
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True})

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

    def get(self, request):
        users = list(User.objects.all().values())
        return Response(users)
