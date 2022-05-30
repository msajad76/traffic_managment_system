# Generated by Django 4.0.4 on 2022-05-16 15:52

from django.db import migrations, IntegrityError
from main.models import VehicleType
import json
import pathlib
from time import sleep

DATA_DIRNAME = 'initial_datas'


def load_owner_and_car_data(apps, schema_editor):
    DATA_FILENAME = 'owners.json'

    Owner = apps.get_model('main', 'Owner')
    Vehicle = apps.get_model('main', 'Vehicle')

    jsonfile = pathlib.Path(__file__).parents[2]/DATA_DIRNAME/DATA_FILENAME
    with open(jsonfile, 'r') as datafile:
        objects = json.load(datafile)
        for obj in objects:
            name = obj.get('name')
            national_code = obj.get('national_code')
            age = obj.get('age')
            total_toll_paid = obj.get('total_toll_paid')
            cars = obj.get('ownerCar')
            owner = Owner.objects.create(
                name=name, national_code=national_code, age=age, total_toll_paid=total_toll_paid)
            for car in cars:
                vehicle_type_label = car.get('type')
                if vehicle_type_label == VehicleType.BIG.label:
                    vehicle_type = VehicleType.BIG.value
                elif vehicle_type_label == VehicleType.SMALL.label:
                    vehicle_type = VehicleType.SMALL.value

                Vehicle.objects.create(id=int(car.get('id')), owner=owner, vehicle_type=vehicle_type, color=car.get(
                    'color'), lenght=car.get('length'), load_valume=car.get('load_valume'))
                


def load_toll_station_data(apps, schema_editor):
    DATA_FILENAME = 'tollStations.json'
    TollStation = apps.get_model('main', 'TollStation')

    jsonfile = pathlib.Path(__file__).parents[2]/DATA_DIRNAME/DATA_FILENAME
    with open(jsonfile, 'r') as datafile:
        objects = json.load(datafile)
        for obj in objects:
            name = obj.get('name')
            toll_per_cross = obj.get('toll_per_cross')
            location = obj.get('location')
            TollStation.objects.create(
                name=name, toll_per_cross=toll_per_cross, location=location)


def load_road_data(apps, schema_editor):
    DATA_FILENAME = 'roads.json'
    Road = apps.get_model('main', 'Road')

    jsonfile = pathlib.Path(__file__).parents[2]/DATA_DIRNAME/DATA_FILENAME
    with open(jsonfile, 'r') as datafile:
        objects = json.load(datafile)
        for obj in objects:
            name = obj.get('name', 'unknown')
            width = obj.get('width')
            geom = obj.get('geom')
            Road.objects.create(name=name, width=width, geom=geom)


def load_node_data(apps, schema_editor):
    DATA_FILENAME = 'all_nodes.json'
    Node = apps.get_model('main', 'Node')

    jsonfile = pathlib.Path(__file__).parents[2]/DATA_DIRNAME/DATA_FILENAME
    with open(jsonfile, 'r') as datafile:
        objects = json.load(datafile)
        for obj in objects:
            car_id = int(obj.get('car'))
            location = obj.get('location')
            date = obj.get('date')
            Node.objects.create(car_id=car_id, location=location, date=date)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_owner_and_car_data),
        migrations.RunPython(load_toll_station_data),
        migrations.RunPython(load_road_data),
        migrations.RunPython(load_node_data),

    ]
