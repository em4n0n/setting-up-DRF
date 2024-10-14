from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import APIView

# Create your views here.
@api_view(['GET', 'POST'])
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        Response({"message":"list of the books"}, status.HTTP_200_OK)
        