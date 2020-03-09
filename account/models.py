from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token


class Account(User):


    def get_token(self):
        try:
            token = Token.objects.get(user=self)
            return str(token)
        except Exception as e:
            print(e)
            return None
