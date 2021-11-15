from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Worker as W
from .serializers import WorkerSerializer, WorkerSerializerOneLevel
from django.contrib.auth.mixins import LoginRequiredMixin

class WorkerAllView(LoginRequiredMixin, generics.ListCreateAPIView):   #only admin can see views
    queryset = W.objects.all()
    serializer_class = WorkerSerializer

class WorkerSelectedLevelView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = W.objects.filter(level__in='0')   #add the required level
    serializer_class = WorkerSerializerOneLevel