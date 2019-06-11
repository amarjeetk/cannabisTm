from rest_framework import serializers 
from .models import Product, Period, Location, Business, Sale, InventoryFinished, InventoryUnfinished
 
class ProductSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Product
        fields = '__all__'
        
    def create(self, validated_data): 
         return Product.objects.create(**validated_data) 
        
class PeriodSerializer(serializers.ModelSerializer): 
    #period_id = serializers.IntegerField()
    # month = serializers.IntegerField()
    # year = serializers.IntegerField()
    class Meta:
        model = Period
        fields = '__all__'
        
    def create(self, validated_data): 
         return Period.objects.create(**validated_data)
         
         
class LocationSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Location
        fields = '__all__'
        
    def create(self, validated_data): 
         return Location.objects.create(**validated_data) 
         
class BusinessSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Business
        fields = '__all__'
        
    def create(self, validated_data): 
         return Business.objects.create(**validated_data) 
         
         
class SaleSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Sale
        fields = '__all__'
        
    def create(self, validated_data): 
         return Sale.objects.create(**validated_data) 
         
class InventoryFinishedSerializer(serializers.ModelSerializer): 

    class Meta:
        model = InventoryFinished
        fields = '__all__'
        
    def create(self, validated_data): 
         return InventoryFinished.objects.create(**validated_data) 
         
         
class InventoryUnfinishedSerializer(serializers.ModelSerializer): 

    class Meta:
        model = InventoryUnfinished
        fields = '__all__'
        
    def create(self, validated_data): 
         return InventoryUnfinished.objects.create(**validated_data) 