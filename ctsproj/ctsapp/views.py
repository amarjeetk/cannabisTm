from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response 
from rest_framework.views import APIView 

from django.shortcuts import get_object_or_404
  
from .models import Product, Period, Location, Business, Sale, InventoryFinished, InventoryUnfinished
from .serializers import ProductSerializer, PeriodSerializer, LocationSerializer, BusinessSerializer, SaleSerializer, InventoryFinishedSerializer, InventoryUnfinishedSerializer
 
class ProductView(APIView): 
    def get(self, request): 
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)        
        return Response({"product": serializer.data}) 

    def post(self, request):
        product = request.data.get('product')

        serializer = ProductSerializer(data=product, many=True)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "OK"})
        
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({"success": "OK"})
        
class PeriodView(APIView): 
    def get(self, request): 
        period = Period.objects.all()
        serializer = PeriodSerializer(period, many=True)        
        return Response({"period": serializer.data}) 

    def post(self, request):
        period = request.data.get('period')

        serializer = PeriodSerializer(data=period, many=True)
        if serializer.is_valid(raise_exception=True):
            period_saved = serializer.save()
        return Response({"success": "OK"})
        
    def delete(self, request, pk):
        period = get_object_or_404(Period, pk=pk)
        period.delete()
        return Response({"success": "OK"})
        

class LocationView(APIView): 
    def get(self, request): 
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)        
        return Response({"location": serializer.data}) 

    def post(self, request):
        location = request.data.get('location')

        serializer = LocationSerializer(data=location, many=True)
        if serializer.is_valid(raise_exception=True):
            location_saved = serializer.save()
        return Response({"success": "OK"})
        
    def delete(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        location.delete()
        return Response({"success": "OK"}) 

class BusinessView(APIView): 
    def get(self, request): 
        year = request.GET.get('year', '2020')
        month = request.GET.get('month', '1')
        business = Business.objects.filter(year=year,month=month)
        serializer = BusinessSerializer(business, many=True)        
        return Response({"business": serializer.data}) 

    def post(self, request):
        business = request.data.get('business')
        serializer = BusinessSerializer(data=business, many=True)
        if serializer.is_valid(raise_exception=True):
            business_saved = serializer.save()
        return Response({"success": "OK"})
        
    def delete(self, request):
        #business = get_object_or_404(Business, pk=pk)
        #business.delete()
        Business.objects.all().delete()
        return Response({"success": "OK"})



class SaleView(APIView): 
    def get(self, request): 
        year = request.GET.get('year', '2020')
        month = request.GET.get('month', '1')
        sale = Sale.objects.filter(year=year,month=month)
        serializer = SaleSerializer(sale, many=True)        
        return Response({"sale": serializer.data}) 

    def post(self, request):
        sale = request.data.get('sale')
        serializer = SaleSerializer(data=sale, many=True)
        if serializer.is_valid(raise_exception=True):
            sale_saved = serializer.save()
        return Response({"success": "OK"})
        
    def delete(self, request):
        #sale = get_object_or_404(Sale, pk=pk)
        #sale.delete()
        Sale.objects.all().delete()
        return Response({"success": "OK"}) 



class InventoryFinishedView(APIView): 
    def get(self, request): 
        year = request.GET.get('year', '2020')
        month = request.GET.get('month', '1')
        inventoryfinished = InventoryFinished.objects.filter(year=year,month=month)
        serializer = InventoryFinishedSerializer(inventoryfinished, many=True)        
        return Response({"inventoryfinished": serializer.data}) 

    def post(self, request):
        inventoryfinished = request.data.get('inventoryfinished')
        serializer = InventoryFinishedSerializer(data=inventoryfinished, many=True)
        if serializer.is_valid(raise_exception=True):
            inventoryfinished_saved = serializer.save()
        return Response({"success": "OK"})
        
    def delete(self, request):
        #inventoryfinished = get_object_or_404(InventoryFinished, pk=pk)
        #inventoryfinished.delete()
        InventoryFinished.objects.all().delete()
        return Response({"success": "OK"})   


class InventoryUnfinishedView(APIView): 
    def get(self, request): 
        year = request.GET.get('year', '2020')
        month = request.GET.get('month', '1')
        inventoryunfinished = InventoryUnfinished.objects.filter(year=year,month=month)
        serializer = InventoryUnfinishedSerializer(inventoryunfinished, many=True)        
        return Response({"inventoryunfinished": serializer.data}) 

    def post(self, request):
        inventoryunfinished = request.data.get('inventoryunfinished')
        serializer = InventoryUnfinishedSerializer(data=inventoryunfinished, many=True)
        if serializer.is_valid(raise_exception=True):
            inventoryunfinished_saved = serializer.save()
        return Response({"success": "OK"})
        
    def delete(self, request):
        #inventoryunfinished = get_object_or_404(InventoryUnfinished, pk=pk)
        #inventoryunfinished.delete()
        InventoryUnfinished.objects.all().delete()
        return Response({"success": "OK"}) 


class ResetView(APIView): 
    def delete(self, request):
        Sale.objects.all().delete()
        Business.objects.all().delete()
        InventoryFinished.objects.all().delete()
        InventoryUnfinished.objects.all().delete()
        return Response({"success": "OK"}) 
        
def deleteData(request):
    Business.objects.all().delete()
    Sale.objects.all().delete()
    InventoryFinished.objects.all().delete()
    InventoryUnfinished.objects.all().delete()
    return Response({"success": "OK"})