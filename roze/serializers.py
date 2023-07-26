from rest_framework import serializers
from .models import Roze, Post 

class RozeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roze
        fields =['id','owner', 'name', 'desc']
        # fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

     class Meta:
        model = Post
        fields = '__all__'