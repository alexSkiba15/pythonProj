from django.conf.urls import url
from store import views

urlpatterns = [
    url(r'^cars/$', views.cars_list),
    url(r'^cars/view$', views.car_view),
    url(r'^cars/view/(?P<car_id>[0-9]+)$', views.car_view),
    url(r'^cars/owners$', views.get_store_data),
]
