import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Car, Owner


class CarsCRUDTest(APITestCase):
    def setUp(self):
        self.car_id = 3000
        self.owner_id = 4000
        self.MAIN_URL = '/cars/'
        Car.objects.create(id=self.car_id, brand='BMW', model='Bgh22', price=12000, date=datetime.datetime.now())
        Owner.objects.create(id=self.owner_id, name='Alex', surname='Test', age=22, email='alex@gmail.com')

    def test_get_cars(self):
        response = self.client.get(self.MAIN_URL, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertNotEquals(response.data, None)

    def test_get_car(self):
        response = self.client.get(f'{self.MAIN_URL}view/car/{self.car_id}', format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertNotEquals(response.data, None)

    def test_incorrect_get_car(self):
        response = self.client.get(f'{self.MAIN_URL}view/car/{self.car_id + 1}', format='json')
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_edit_car(self):
        response = self.client.put(f'{self.MAIN_URL}view/car/3000', {'brand': 'Audi'}, format='json')
        self.assertEquals(response.data.get('result'), 1)
        car = Car.objects.get(id=self.car_id)
        self.assertEquals(car.brand, 'Audi')

    def test_incorrect_edit_car(self):
        response = self.client.put(f'{self.MAIN_URL}view/car/3000', {'price': '30000000000sdfsdf'}, format='json')
        self.assertEquals(response.data.get('result'), 0)
        car = Car.objects.get(id=self.car_id)
        self.assertNotEquals(car.price, '30000000000sdfsdf')

    def test_delete_car(self):
        response = self.client.delete(f'{self.MAIN_URL}view/car/3000', format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('result'), 1)

    def test_get_owners_for_create_car(self):
        response = self.client.get(f'{self.MAIN_URL}view/car/', format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_car(self):
        response = self.client.post(f'{self.MAIN_URL}view/car/', {'brand': 'Audi', 'model': 'A8', 'price': 30000,
                                                                  'data': datetime.datetime.now()}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('result'), 1)

    def test_incorrect_create_car(self):
        response = self.client.post(f'{self.MAIN_URL}view/car/', {'brand': 'Audi', 'model': 'A8', 'price': 'test',
                                                                  'data': datetime.datetime.now()}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('result'), 0)

    def test_get_owners(self):
        response = self.client.get(f'{self.MAIN_URL}owners', format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_owner_for_edit(self):
        response = self.client.get(f'{self.MAIN_URL}view/owner/{self.owner_id}', format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertNotEquals(response.data, None)

    def test_get_incorrect_owner_for_edit(self):
        response = self.client.get(f'{self.MAIN_URL}view/owner/{self.owner_id+1}', format='json')
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_edit_correct_owner(self):
        response = self.client.put(f'{self.MAIN_URL}view/owner/{self.owner_id}',
                                   {'name': 'TEST', 'surname': 'TEST',
                                    'age': 33, 'email': 'test@test.com'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        owner = Owner.objects.get(id=self.owner_id)
        self.assertEquals(owner.age, 33)
        self.assertNotEquals(owner.name, 'Alex')

    def test_edit_incorrect_owner_for_edit(self):
        response = self.client.put(f'{self.MAIN_URL}view/owner/{self.owner_id}',
                                   {'name': 'TEST', 'surname': 'TEST',
                                    'age': 333, 'email': 'test'}, format='json')
        owner = Owner.objects.get(id=self.owner_id)
        self.assertEquals(response.data.get('result'), 0)
        self.assertEquals(owner.age, 22)

    def test_correct_delete_owner(self):
        response = self.client.delete(f'{self.MAIN_URL}view/owner/{self.owner_id}', forma='json')
        self.assertEquals(response.data.get('result'), 1)
        try:
            owner = Owner.objects.get(id=self.owner_id)
        except Owner.DoesNotExist as e:
            print(e)
            self.assertEquals(str(e), 'Owner matching query does not exist.')

    def test_correct_create_owner(self):
        response = self.client.post(f'{self.MAIN_URL}view/owner',
                                    {'name': 'User', 'surname': 'UserSurname',
                                     'age': 23, 'email': 'test@test.net'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('result'), 1)

    def test_incorrect_create_owner(self):
        response = self.client.post(f'{self.MAIN_URL}view/owner',
                                    {'name': 'User', 'surname': 'UserSurname',
                                     'age': 2333, 'email': 'testest.net'}, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('result'), 0)

    def test_scrapper_cars(self):
        response = self.client.get(f'{self.MAIN_URL}scraper_cars', format='json')
        self.assertEquals(response.data.get('result'), 1)

    def test_create_user(self):
        response = self.client.post('/register/',
                                    {'username': 'Test', 'first_name': 'test', 'last_name': 'last test',
                                     'password': '123456', 'email': 'test@tma.com'},
                                    format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data.get('result'), 1)
