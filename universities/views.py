from rest_framework.response import Response
from rest_framework.views import APIView

from universities.models import University
from universities.serializers import UniversitiesSerializer


# Create your views here.

class UniversitiesData(APIView):

    def post(self, request):
        data = list(request.data)
        for univers in data:
            serializer = UniversitiesSerializer(data=univers)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"ok": True})

    def get(self, request):
        data = list(University.objects.all().values())
        return Response(data)
