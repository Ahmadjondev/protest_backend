import random

from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView

from battle.models import OneToOne
from battle.serializer import OneToOneSerializer
from user.models import User
from user.serializers import UserSerializer


# Create your views here.
def getUser(user):
    serializer = UserSerializer(user)
    return dict(serializer.data)


class OneToOneBattle(APIView):

    def post(self, request):
        data = request.data
        if data['action'] == 'create_room':
            # code_room: str = str(random.randint(10000, 999999))
            # data['code'] = code_room
            serializer = OneToOneSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({'ok': True, 'id': serializer.data['id']})

        if data['action'] == 'join_room':
            try:
                one = OneToOne.objects.get()
                battle = model_to_dict(one)
                if bool(battle['is_finished']):
                    return Response({'ok': False, 'error': "Bunday o'yin mavjud emas"})
                if bool(battle['is_started']):
                    return Response({'ok': False, 'error': "O'yin boshlangan"})
                battle['user_2'] = int(data['id'])
                # battle['is_started'] = True
                serializer = OneToOneSerializer(one, data=battle)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                user_1 = User.objects.get()
                game = dict(serializer.data)
                game['user_1'] = getUser(user_1),
                return Response({'ok': True, 'game': game})
            except:
                return Response({'ok': False, 'error': "Bunday o'yin mavjud emas"})
        one = OneToOne.objects.get()
        battle = model_to_dict(one)

        if data['action'] == 'is_joined':
            if battle['user_2'] == '' or battle['user_2'] is None:
                return Response({'ok': False})
            else:
                return Response({'ok': True})

        if data['action'] == 'game':
            user1 = User.objects.get()
            user2 = User.objects.get()
            game = dict(model_to_dict(one))
            game['user_1'] = getUser(user1)
            game['user_2'] = getUser(user2)
            return Response({'ok': game})

        if data['action'] == 'current_question_1':
            battle['current_question_1'] += 1
            serializer = OneToOneSerializer(one, data=battle)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'question': battle['current_question_1']})

        if data['action'] == 'current_question_2':
            battle['current_question_2'] += 1
            serializer = OneToOneSerializer(one, data=battle)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'question': battle['current_question_2']})

        if data['action'] == 'correct_1':
            battle['correct_1'] += 1
            serializer = OneToOneSerializer(one, data=battle)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'correct': battle['correct_1']})

        if data['action'] == 'correct_2':
            battle['correct_2'] += 1
            serializer = OneToOneSerializer(one, data=battle)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'ok': True, 'correct': battle['correct_1']})

        if data['action'] == 'finished':
            battle['is_finished'] = True
            if int(battle['correct_1']) > int(battle['correct_2']):
                battle['winner'] = battle['user_1']
            elif int(battle['correct_1']) == int(battle['correct_2']):
                battle['winner'] = "Durrang"
            else:
                battle['winner'] = battle['user_2']
            serializer = OneToOneSerializer(one, data=battle)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        if data['action'] == 'delete':
            instance = OneToOne.objects.get()
            instance.delete()
            return Response({'ok': True})

    def get(self, request):
        alls = list(OneToOne.objects.all().values())
        return Response(alls)
