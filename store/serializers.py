from rest_framework import serializers

from store.models import Car, Owner


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model', 'brand', 'price', 'date', 'ownerId')


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'name', 'surname', 'age', 'email')
