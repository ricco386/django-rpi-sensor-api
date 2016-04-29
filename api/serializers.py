from gui.models import Unit, Sensor, Node, Measurement
from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('name',)


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'units')


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('name', 'head', 'token', 'sensors')


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('node', 'sensor', 'date', 'value', 'unit')
