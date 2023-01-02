from django.shortcuts import render
from api.serializers import ProductSerializer,ProductDetailSerializer
from product.models import Product
from api.models import ProductDetail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import json

# Create your views here.
class ProductsView(APIView):
    def get(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)


    def existing_product(self,prodname):        
        try:
            queryset = Product.objects.get(name=prodname)
            return queryset
        except Product.DoesNotExist:
            return None


    def post(self,request):    
        serializer = ProductSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
            # print(request.data)
            # return Response({"Post":"true"})
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def single_product(self,id_arg):
        try:
            queryset = Product.objects.get(id=id_arg)
            return queryset
        except Product.DoesNotExist:
            return None

    def get(self,request,id_arg):
        # queryset = Product.objects.get(id=id_arg)
        queryset = self.single_product(id_arg)
        if queryset:
            serializer = ProductSerializer(queryset)
            return Response(serializer.data)
        else:
            return Response(
                {"msg":f"Product with the id :{id_arg} does not exist"},
                status.HTTP_400_BAD_REQUEST
                
                )
    

# class ProductDetailView(APIView):
def detail_View(request):
    queryset = ProductDetail.objects.all()
        # serializer = ProductDetailSerializer(queryset,many=True)        
        # return Response(serializer.data)
        # queryset = {"name":"selva"}
    template = r'templates\\api\\product.html'
    return render(request,template,{'queryset':queryset})





