import logging

import requests
import datetime
import re

from bs4 import BeautifulSoup
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from store.models import Car, Owner
from store.serializers import CarsSerializer, OwnerSerializer, UserSerializer


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


def create_user(request):
    user_data = JSONParser().parse(request)
    user_serializer = UserSerializer(data=user_data)
    if user_serializer.is_valid():
        user_serializer.save()

        return Response({
            "result": 1,
            "error": ''
        })

    return Response({
        "result": 0,
        "error": 'error'
    })


def scraper_cars():
    k = 0
    try:
        page = 2
        for page in range(5):
            url = f'https://planetavto.ua/ru/page={page};'
            response = requests.get(url, headers={
                'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) "
                              "Chrome/24.0.1312.27 Safari/537.17"})
            soup = BeautifulSoup(response.text, 'html.parser')
            table_cars = soup.find('section', class_='main_products').findAll('article', class_='product_item')
            for car in table_cars:
                k += 1
                print(f'Car - {k}')
                brand_model = car.find('a', class_='prod-link').text
                brand_model_str = brand_model.__str__()
                t = re.search(r'([\w-]+) (.+)', brand_model_str)
                brand = t.group(1).capitalize()
                model = t.group(2).capitalize()

                year_ = car.find('span', class_='year-show').text
                year = int(year_[2:])

                car_id = car.find('a', class_='prod-link').get('id')
                price = __scraper_price(car_id)

                det = datetime.date(year, 1, 1)

                data = {
                    'brand': brand,
                    'model': model,
                    'price': price,
                    'date': det
                }

                car_serializer = CarsSerializer(data=data)

                if car_serializer.is_valid():
                    car_serializer.save()
    except Exception as e:
        logging.error(f'Failed. - {e}')

    return Response({
        "result": 1,
        "error": 'error'
    })


def __scraper_price(car_id):
    try:
        url = f'https://planetavto.ua/ru/products/{car_id}'
        response = requests.get(url, headers={
            'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) "
                          "Chrome/24.0.1312.27 Safari/537.17"})
        soup = BeautifulSoup(response.text, 'html.parser')
        price_car = soup.find('p', class_='full_price').find('b').text
        return int(price_car.replace(' ', ''))
    except Exception as e:
        logging.error(f'Failed. - {e}')
