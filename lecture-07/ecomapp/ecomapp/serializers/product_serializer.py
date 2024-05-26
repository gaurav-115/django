from rest_framework import serializers
from ecomapp.models import Product, Dairyproduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class DairyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairyproduct
        fields = "__all__"
