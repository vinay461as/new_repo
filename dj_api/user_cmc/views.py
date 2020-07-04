from django.shortcuts import render

from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import MemberSerializer
from .models import *
from rest_framework import status

# Create your views here.

class MemberView (APIView):

    def get (self, request):
        member= Member.objects.all ()
        serializer = MemberSerializer(member, many=True)
        return Response(serializer.data)