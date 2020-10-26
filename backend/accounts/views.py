from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView


class UserAPI(APIView):
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


    # def put(self, request):
    #     request.user.update(request.data)
    #     serializer = UserSerializer(request.user)
    #     return Response(serializer.data)
