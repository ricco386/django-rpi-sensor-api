from gui.models import Unit, Sensor, Node, Measurement
from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'name',)


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'units')


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', 'token', 'desc', 'location', 'ip', 'sensors')


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('node', 'sensor', 'date', 'value', 'unit')
