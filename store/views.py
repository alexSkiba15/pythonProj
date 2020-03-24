from django.http import HttpResponse
from rest_framework.decorators import api_view

from store.models import Car, Owner
from store.helper import get_cars, get_car_for_edit, update_car, get_owners, create_car, delete_car, \
    get_cars_with_owner, get_owner_for_edit, update_owner, delete_owner, create_owner, scraper_cars, create_user


@api_view(['GET'])
def cars_list(request):
    return get_cars()



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def car_view(request, car_id=None):
    if car_id is not None:
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            return get_car_for_edit(car)
        elif request.method == 'PUT':
            return update_car(car, request)
        elif request.method == 'DELETE':
            return delete_car(car)
    else:
        if request.method == 'GET':
            return get_owners()
        elif request.method == 'POST':
            return create_car(request)


@api_view(['GET'])
def get_store_data(request):
    return get_cars_with_owner()


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def owner_view(request, owner_id=None):
    if owner_id is not None:
        try:
            owner = Owner.objects.get(id=owner_id)
        except Owner.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            return get_owner_for_edit(owner)
        elif request.method == 'PUT':
            return update_owner(owner, request)
        elif request.method == 'DELETE':
            return delete_owner(owner)
    else:
        if request.method == 'POST':
            return create_owner(request)


@api_view(['GET'])
def scraper_car(request):
    return scraper_cars()


@api_view(['POST'])
def create_users(request):
    return create_user(request)
