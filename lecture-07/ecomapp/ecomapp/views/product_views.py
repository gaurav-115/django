from rest_framework.response import Response
from rest_framework.views import APIView
from ecomapp.models import Product
from ecomapp.serializers import ProductSerializer

class ListCreateProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data, status=200)

    def post(self, request):
        data = request.data
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response(decoded_data.errors, status=400)
        decoded_data.save()
        return Response(decoded_data.data, status=200)
        # product = Product.objects.create(
        #     name=data['name'],
        #     price=data['price'],
        #     description=data['description']
        # )
        # return Response({"product":product})