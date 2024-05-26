from rest_framework.response import Response
from rest_framework.views import APIView
from ecomapp.models import Product,Dairyproduct
from ecomapp.serializers import ProductSerializer, DairyProductSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView

class ListCreateProductAPIView(APIView):
    def get(self, request):
        # products = Product.objects.all().filter(price__gte=30)
        # products = Product.objects.all().filter(price__gte=30).first()
        products = Product.objects.raw("select * from ecomapp_product;")
        '''when passing list many=True is mandatory'''
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

class DairyListCreateAPIView(ListCreateAPIView):
    queryset = Dairyproduct.objects.all()
    serializer_class = DairyProductSerializer

class RetrieveUpdateAPIViewDairyAPIView(RetrieveUpdateAPIView):
    queryset = Dairyproduct.objects.all()
    serializer_class = DairyProductSerializer

