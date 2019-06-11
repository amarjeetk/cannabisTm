from django.urls import path 
from . import views
from .views import ProductView, PeriodView, LocationView, BusinessView, SaleView, InventoryFinishedView, InventoryUnfinishedView, ResetView

app_name = "ctsapp" 
 
# app_name will help us do a reverse look-up latter. 
urlpatterns = [ 
     path('product/', ProductView.as_view()),
     path('product/<int:pk>', ProductView.as_view()),
     path('period/', PeriodView.as_view()),
     path('period/<int:pk>', PeriodView.as_view()),
     path('location/', LocationView.as_view()),
     path('location/<int:pk>', LocationView.as_view()),
     path('business/', BusinessView.as_view()),
     path('business/<int:pk>', BusinessView.as_view()),
     path('sale/', SaleView.as_view()),
     path('sale/<int:pk>', SaleView.as_view()),
     path('inventoryfinished/', InventoryFinishedView.as_view()),
     path('inventoryfinished/<int:pk>', InventoryFinishedView.as_view()),
     path('inventoryunfinished/', InventoryUnfinishedView.as_view()),
     path('inventoryunfinished/<int:pk>', InventoryUnfinishedView.as_view()),
     path('reset/', ResetView.as_view()),
 ] 

