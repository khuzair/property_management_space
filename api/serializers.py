from rest_framework import serializers
from .models import Property


class PropertyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class CarListPropertyModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('property_name', 'address', 'city', 'state')
        read_only_fields = ('city',)
        extra_kwargs = {
            'property_name': {'write_only': True},
            'address': {'write_only': True},
            'state': {'write_only': True}
        }