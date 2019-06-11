from django.db import models

# Create your models here.

class Location(models.Model):
    location_id = models.PositiveIntegerField(primary_key=True)
    location_abbr = models.CharField("Province Abbreviation",max_length=2)
    location = models.CharField("Province",max_length=50)
    
    def __str__(self):
        return self.location
        
    class Meta:
        verbose_name_plural = "Location"

class Period(models.Model):
    period_id = models.PositiveIntegerField(primary_key=True)
    month = models.PositiveSmallIntegerField("Month")
    year = models.PositiveSmallIntegerField("Year")
    
    def __str__(self):
        return str(self.period_id)
        
    class Meta:
        verbose_name_plural = "Period"
        
 
class Product(models.Model):
    product_id = models.PositiveIntegerField(primary_key=True)
    product = models.CharField("Product Type",max_length=100)
    
    def __str__(self):
        return self.product
        
    class Meta:
        verbose_name_plural = "Product"
 
class Business(models.Model):
    month = models.PositiveSmallIntegerField("Month")
    year = models.PositiveSmallIntegerField("Year")
    licence = models.CharField("Licence ID",max_length=100)
    employee_management = models.PositiveSmallIntegerField("Management Employees")
    employee_administrative = models.PositiveSmallIntegerField("Administrative Employees")
    employee_production = models.PositiveSmallIntegerField("Production Employees")
    employee_sales = models.PositiveSmallIntegerField("Sales Employees")
    employee_other = models.PositiveSmallIntegerField("Other Employees")
    capacity_flowering_area = models.PositiveIntegerField("Flowering Area Utilized Capacity")
    capacity_mother_room = models.PositiveIntegerField("Mother Room Capacity")
    capacity_cloning_room = models.PositiveIntegerField("Cloning Room Capacity")
    capacity_drying_room = models.PositiveIntegerField("Drying Room Capacity")
    
    
    def __str__(self):
        return self.licence
        
    class Meta:
        verbose_name_plural = "Business"
        
class Sale(models.Model):
    month = models.PositiveSmallIntegerField("Month")
    year = models.PositiveSmallIntegerField("Year")
    licence = models.CharField("Licence ID",max_length=100)
    location = models.CharField("Province",max_length=25)
    product = models.CharField("Product Type",max_length=100)
    consumption = models.CharField("Consumption Type",max_length=100)
    distribution = models.CharField("Distribution Type",max_length=100)
    quantity = models.DecimalField("Quantity",max_digits=15,decimal_places=3)
    
    def __str__(self):
        return self.licence
        
    class Meta:
        verbose_name_plural = "Sales"   

class InventoryUnfinished(models.Model):
    month = models.PositiveSmallIntegerField("Month")
    year = models.PositiveSmallIntegerField("Year")
    licence = models.CharField("Licence ID",max_length=100)
    product = models.CharField("Product Type",max_length=100)
    opening_inventory = models.DecimalField("Opening Inventory",max_digits=15,decimal_places=3)
    addition_total_production = models.DecimalField("Total Production",max_digits=15,decimal_places=3)
    addition_purchased_cultivator = models.DecimalField("Quantity Purchased/Transferred from Cultivators",max_digits=15,decimal_places=3)
    addition_purchased_processor = models.DecimalField("Quantity Purchased/Transferred from Processors",max_digits=15,decimal_places=3)
    addition_purchased_hemp = models.DecimalField("Quantity Purchased/Transferred from Hemp",max_digits=15,decimal_places=3)
    addition_purchased_tester = models.DecimalField("Quantity Purchased/Transferred from Testers or Researchers",max_digits=15,decimal_places=3)
    addition_imported = models.DecimalField("Quantity Imported into Canada",max_digits=15,decimal_places=3)
    addition_returned = models.DecimalField("Quantity Returned",max_digits=15,decimal_places=3)
    reduction_processed = models.DecimalField("Quantity Processed",max_digits=15,decimal_places=3)
    reduction_packaged = models.DecimalField("Quantity Packaged and Labeled",max_digits=15,decimal_places=3)
    reduction_sold_cultivator = models.DecimalField("Quantity Sold/Transferred to Cultivators",max_digits=15,decimal_places=3)
    reduction_sold_processor = models.DecimalField("Quantity Sold/Transferred to Processors",max_digits=15,decimal_places=3)
    reduction_sold_hemp = models.DecimalField("Quantity Sold/Transferred to Hemp",max_digits=15,decimal_places=3)
    reduction_sold_tester = models.DecimalField("Quantity Sold/Transferred to Testers or Researchers",max_digits=15,decimal_places=3)
    reduction_exported = models.DecimalField("Quantity Exported Outside Canada",max_digits=15,decimal_places=3)
    reduction_drying_loss = models.DecimalField("Adjustment for Drying/Processing Loss",max_digits=15,decimal_places=3)
    reduction_destroyed = models.DecimalField("Quantity Destroyed",max_digits=15,decimal_places=3)
    reduction_stolen = models.DecimalField("Quantity Lost/Stolen",max_digits=15,decimal_places=3)
    reduction_returned = models.DecimalField("Quantity Returned",max_digits=15,decimal_places=3)
    reduction_other = models.DecimalField("Other Reductions",max_digits=15,decimal_places=3)
    
    def __str__(self):
        return self.licence
        
    class Meta:
        verbose_name_plural = "Unfinished Inventory"  


class InventoryFinished(models.Model):
    month = models.PositiveSmallIntegerField("Month")
    year = models.PositiveSmallIntegerField("Year")
    licence = models.CharField("Licence ID",max_length=100)
    product = models.CharField("Product Type",max_length=100)
    opening_inventory = models.DecimalField("Opening Inventory",max_digits=15,decimal_places=3)
    addition_packaged = models.DecimalField("Quantity Packaged",max_digits=15,decimal_places=3)
    addition_purchased = models.DecimalField("Quantity Purchased/Transferred",max_digits=15,decimal_places=3)
    addition_returned = models.DecimalField("Quantity Returned",max_digits=15,decimal_places=3)
    addition_other = models.DecimalField("Additions Other",max_digits=15,decimal_places=3)
    reduction_sold = models.DecimalField("Quantity Sold/Transferred",max_digits=15,decimal_places=3)
    reduction_destroyed = models.DecimalField("Quantity Destroyed",max_digits=15,decimal_places=3)
    reduction_stolen = models.DecimalField("Quantity Lost/Stolen",max_digits=15,decimal_places=3)
    reduction_returned = models.DecimalField("Quantity Returned",max_digits=15,decimal_places=3)
    reduction_other = models.DecimalField("Other Reductions",max_digits=15,decimal_places=3)
    
    def __str__(self):
        return self.licence
        
    class Meta:
        verbose_name_plural = "Finished Inventory"          