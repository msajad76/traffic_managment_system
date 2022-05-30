from django.contrib.gis import geos
from django.contrib.gis.measure import D
from django.db.models import F, Max, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, generics, status
from rest_framework.response import Response

from main import models, serializers

from .filters import VehicleFilter


class VehicleView(generics.ListCreateAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VehicleFilter


class OwnerView(generics.ListCreateAPIView):
    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerSerializer


class VehicleStatusView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.NodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicle_type']

    def list(self, request, *args, **kwargs):
        try:
            toll_station = models.TollStation.objects.get(
                name=request.GET.get('toll_station', 'عوراضی 1'))
        except models.TollStation.DoesNotExist:
            raise exceptions.NotFound('toll station does not exits')

        queryset = self.filter_queryset(self.get_queryset())
        qs = queryset.annotate(last_location_date=Max('node__date'))

        last_nodes = []
        last_nodes_pk = []
        for i in qs:
            node = models.Node.objects.get(car=i, date=i.last_location_date)
            last_nodes.append(node)
            last_nodes_pk.append(node.pk)

        try:
            distance = int(request.GET.get('distance', 600))
        except:
            raise exceptions.NotAcceptable('Invalid distance')
        result_queryset = models.Node.objects.filter(
            pk__in=last_nodes_pk, location__distance_lte=(toll_station.location, D(m=distance)))
        serializer = self.get_serializer(result_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
