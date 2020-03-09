from django.conf.urls import url
from store import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^cars/$', views.cars_list),
    url(r'^cars/view/car/$', views.car_view),
    url(r'^cars/view/car/(?P<car_id>[0-9]+)$', views.car_view),
    url(r'^cars/view/owner$', views.owner_view),
    url(r'^cars/view/owner/(?P<owner_id>[0-9]+)$', views.owner_view),
    url(r'^cars/owners$', views.get_store_data),
    url(r'^cars/scraper_cars$', views.scraper_car),
    url(r'^register/$', views.create_users),
    url(r'^api-token-auth/$', obtain_auth_token, name='api_token_auth'),
]
