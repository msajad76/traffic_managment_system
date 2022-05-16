from django.db import models
from django.contrib.gis.db import models as gis_models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Owner(models.Model):
    name = models.CharField(max_length=50)
    national_code = models.CharField(
        max_length=10, validators=[MinLengthValidator(10)])
    age = models.PositiveSmallIntegerField()
    total_toll_paid = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self) -> str:
        return self.name


class VehicleType(models.TextChoices):
    SMALL = 'S', _('small')
    BIG = 'B', _('big')


class Vehicle(models.Model):

    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    vehicle_type = models.CharField(
        "type", max_length=1, choices=VehicleType.choices)
    color = models.CharField(max_length=10)
    lenght = models.DecimalField(max_digits=3, decimal_places=1)
    load_valume = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner'], condition=models.Q(
                vehicle_type='B'), name='big_type_unique')
        ]

    def __str__(self) -> str:
        return f'{self.owner}, {self.get_vehicle_type_display()}, {self.color}'


class TollStation(models.Model):
    name = models.CharField(max_length=30,  unique=True)
    toll_per_cross = models.DecimalField(max_digits=11, decimal_places=0)
    location = gis_models.PointField()


class Road(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default='unknown')
    width = models.DecimalField(max_digits=18, decimal_places=15)
    geom = gis_models.MultiLineStringField()

    class Meta:
        unique_together = [['name', 'width']]

    def __str__(self) -> str:
        return f'{self.name, self.width}'


class Node(models.Model):
    car = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    location = gis_models.PointField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.car} at {self.date}'
