from rest_framework import serializers
from api.models import Mobiles

class MobileSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    band=serializers.CharField()
    specs=serializers.CharField()
    price=serializers.IntegerField()


class MobileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobiles
        fields="__all__"
