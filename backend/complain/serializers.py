from rest_framework import serializers
from .models import Complain


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = '__all__'


class ComplainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ('id', 'author', 'role','description','reply')


class ComplainRespSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ('id','reply')
