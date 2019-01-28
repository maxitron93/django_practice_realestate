from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model): # singluar version
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) # foreign key of another table
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True) # blank=True means this is optional
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # location inside the media folder
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # location inside the media folder
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # location inside the media folder
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # location inside the media folder
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # location inside the media folder
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # location inside the media folder
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # location inside the media folder
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  
  def __str__(self):
    return self.title