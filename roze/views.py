from django.shortcuts import render
from .models import Roze
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import RozeSerializer
# Create your views here.

# class RozeListView(ListAPIView):
class RozeListView(ListCreateAPIView):

    queryset = Roze.objects.all()
    serializer_class = RozeSerializer


class RozeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Roze.objects.all()
    serializer_class = RozeSerializer
