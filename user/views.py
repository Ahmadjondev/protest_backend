from django.forms import model_to_dict

from .models import User, Badge
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
import os


# Create your views here.
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
            try:
                serializer = UserSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(
                    {'ok': True, 'id': serializer.data['id'], 'message': "Foydanunchi muvaffaqiyatli yaratildi"})
            except:
                return Response({'ok': False, 'error': 'User yaratilmadi'})

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
                    user = User.objects.get()
                else:
                    user = User.objects.get()
                serializer = UserSerializer(user)
                return Response({'ok': True, 'id': serializer.data['id']})
            except:
                return Response({'ok': False})


class UserData(APIView):
    def post(self, request):
        data = request.data
        if data['action'] == 'get_user':
            user = User.objects.get()
            serializer = UserSerializer(user)
            return Response(serializer.data)

        if data['action'] == 'update_coins':
            user = User.objects.get()
            json = model_to_dict(user)
            json['coins'] += int(data['coins'])
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'message': "Tanga qoshildi"})

        if data['action'] == 'update_ball':
            user = User.objects.get()
            json = model_to_dict(user)
            json['ball'] += (data['ball'])
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'message': "Ball yangilandi"})

        if data['action'] == 'update_online':
            user = User.objects.get()
            json = model_to_dict(user)
            json['is_online'] = bool(data['is_online'])
            serializer = UserSerializer(user, data=json)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True})

        if data['action'] == 'change_image':
            user = User.objects.get()
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

    # def get(self, request, *args, **kwargs):
    #     try:
    #         user = get_user_model().objects.get(pk=kwargs['req_user_pk'])
    #     except get_user_model().DoesNotExist:
    #         user = None
    #     try:
    #         post = Post.objects.get(pk=kwargs['post_pk'])
    #     except Post.DoesNotExist:
    #         post = None
    #     if user is not None and post is not None:
    #         if user in post.likes.all():
    #             post.likes.remove(user)
    #             message(user.username + " unliked the post '{}'".format(post.pk))
    #         else:
    #             post.likes.add(user)
    #             message(user.username + " liked the post '{}'".format(post.pk))
    #         return Response(status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
    #                     data={"error": "Invalid pk values"})


class UserBadge(APIView):
    def get(self, request):
        try:
            user = User.objects.get()
            serializer = UserSerializer(user)
        except User.DoesNotExist:
            user = None
        try:
            badge = Badge.objects.get()
        except Badge.DoesNotExist:
            badge = None

        if user is not None and badge is not None:
            if user in badge.objects.all():
                print("This have a Badge")
            else:
                badge.add(user)
        a = UserSerializer(user)
        return Response({'ok': a.data})
