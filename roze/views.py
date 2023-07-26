from django.shortcuts import render
from .models import Roze,Post
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import RozeSerializer,PostSerializer

from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# class ThingListView(ListAPIView):
class RozeListView(ListCreateAPIView):

    queryset = Roze.objects.all()
    serializer_class = RozeSerializer


class RozeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Roze.objects.all()
    serializer_class = RozeSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PostListView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class  PostDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]