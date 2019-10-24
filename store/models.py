from django.db import models


class Owner(models.Model):
    id = models.FloatField
    name = models.CharField(max_length=20, blank=False, default='')
    surname = models.CharField(max_length=20, blank=False, default='')
    age = models.IntegerField(blank=False, default=0)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Owners'
        verbose_name = 'Owner'
        ordering = ['name']


class Car(models.Model):
    id = models.FloatField
    brand = models.CharField(max_length=10, blank=False, default='')
    model = models.CharField(max_length=15, blank=False, default='')
    price = models.FloatField(max_length=9, blank=False, default=0)
    date = models.DateField(blank=False)
    ownerId = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='cars_owner',
                                verbose_name='Owner', null=True)

    class Meta:
        verbose_name_plural = 'Cars'
        verbose_name = 'Car'
        ordering = ['brand']
