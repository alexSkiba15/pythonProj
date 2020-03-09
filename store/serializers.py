from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from store.models import Car, Owner


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model', 'brand', 'price', 'date', 'ownerId')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'name', 'surname', 'age', 'email')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
