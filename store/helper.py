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
    car_serializer = CarsSerializer(car)
    owner_serializer = OwnerSerializer(Owner.objects.all(), many=True)

    return Response({
        "car": car_serializer.data,
        "owners": owner_serializer.data,
        "error": ''
    })


def update_car(car, request):
    car_data = JSONParser().parse(request)
    car_serializer = CarsSerializer(car, data=car_data)
    if car_serializer.is_valid():
        car_serializer.save()

        return Response({
            "result": 1,
            "error": ''
        })

    return Response({
        "result": 0,
        "error": 'incorrect data'
    })


def get_owners():
    owner_serializer = OwnerSerializer(Owner.objects.all(), many=True)

    return Response({
        "owners": owner_serializer.data
    })


def create_car(request):
    car_data = JSONParser().parse(request)
    car_serializer = CarsSerializer(data=car_data)
    print(car_data)
    if car_serializer.is_valid():
        car_serializer.save()

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


def get_owner_for_edit(owner):
    owner_serializer = OwnerSerializer(owner)

    return Response({
        "owner": owner_serializer.data,
        "error": ''
    })


def update_owner(owner, request):
    owner_data = JSONParser().parse(request)
    owner_serializer = OwnerSerializer(owner, data=owner_data)
    print('im here')
    if owner_serializer.is_valid():
        owner_serializer.save()

        return Response({
            "result": 1,
            "error": ''
        })

    return Response({
        "result": 0,
        "error": 'incorrect data'
    })


def delete_owner(owner):
    owner.delete()

    return Response({
        "result": 1,
        "error": ''
    })


def create_owner(request):
    owner_data = JSONParser().parse(request)
    owner_serializer = OwnerSerializer(data=owner_data)
    print(owner_data)
    if owner_serializer.is_valid():
        owner_serializer.save()

        return Response({
            "result": 1,
            "error": ''
        })

    return Response({
        "result": 0,
        "error": 'error'
    })
