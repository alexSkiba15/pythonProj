from django.contrib import admin

from .models import Car, Owner


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'price', 'date', 'ownerId')
    list_display_links = ('brand', 'model')
    search_fields = ('date', 'model')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'surname')


admin.site.register(Car, CarAdmin)
admin.site.register(Owner, OwnerAdmin)
