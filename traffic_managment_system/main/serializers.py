from rest_framework import serializers
from main import models


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Owner
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'

    def to_representation(self, obj):
        self.fields['owner'] = OwnerSerializer()
        return super().to_representation(obj)


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Node
        fields = '__all__'

    def to_representation(self, obj):
        self.fields['car'] = VehicleSerializer()
        return super().to_representation(obj)
