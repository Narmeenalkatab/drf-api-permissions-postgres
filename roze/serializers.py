from rest_framework import serializers
from .models import Roze

class RozeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roze
        fields =['id','owner', 'name', 'desc']
        # fields = '__all__'