from rest_framework.parsers import JSONParser

from store.models import Car, Owner
from store.serializers import CarsSerializer, OwnerSerializer
from rest_framework.response import Response


def get_cars():
    cars_serializer = CarsSerializer(Car.objects.all(), many=True)

    return Response({
        "cars": cars_serializer.data,
        "error": ''
    })


def get_car_for_edit(car):
    cars_serializer = CarsSerializer(car)
    owner_serializer = OwnerSerializer(Owner.objects.all(), many=True)

    return Response({
        "car": cars_serializer.data,
        "owners": owner_serializer.data,
        "error": ''
    })


def update_car(car, request):
    car_data = JSONParser().parse(request)
    cars_serializer = CarsSerializer(car, data=car_data)
    if cars_serializer.is_valid():
        cars_serializer.save()

        return Response({
            "result": 1,
            "error": ''
        })

    return Response({
        "car": cars_serializer.data,
        "error": 'incorrect data'
    })


def get_owners():
    owner_serializer = OwnerSerializer(Owner.objects.all(), many=True)

    return Response({
        "owners": owner_serializer.data
    })


def create_car(request):
    cars_data = JSONParser().parse(request)
    cars_serializer = CarsSerializer(data=cars_data)
    print(cars_data)
    if cars_serializer.is_valid():
        cars_serializer.save()
        return Response({
            "result": 1,
            "error": ''
        })
    return Response({
        "result": 0,
        "error": 'error'
    })


def delete_car(car):
    car.delete()

    return Response({
        "result": 1,
        "error": ''
    })


def get_cars_with_owner():
    owner_serializer = OwnerSerializer(Owner.objects.all(), many=True)
    cars_serializer = CarsSerializer(Car.objects.all().exclude(ownerId_id=None), many=True)

    return Response({
        "cars": cars_serializer.data,
        "owners": owner_serializer.data
    })
