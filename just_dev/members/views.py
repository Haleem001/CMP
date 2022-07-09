from django.shortcuts import render
import imp
from django.shortcuts import render
from .serializers import MemberSerializer
from .models import Member
from rest_framework import viewsets


# Create your views here.
class MemberViewSet(viewsets.ModelViewSet):
    serializer_class =MemberSerializer
    queryset = Member.objects.all()
