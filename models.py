from django.db import models
from django.urls import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your models here.
class Items(models.Model):
    item_name=models.CharField(max_length=32)
    item_price=models.CharField(max_length=8)
    item_image=models.ImageField()
    item_description=models.CharField(max_length=64)
    contact_number=models.CharField(max_length=32)
    
    def __str__(self):
        return self.item_name+'  '+self.item_price
    
    #def get_absolute_url(self):
        #return HttpResponseRedirect(reverse("buy"))
    
    
class ExchangeItems(models.Model):
    exchange_item_name=models.CharField(max_length=32)
    exchange_item_price=models.CharField(max_length=8)
    exchange_item_image=models.FileField()
    exchange_items_description=models.CharField(max_length=64)
    
    def __str__(self):
        
        return self.exchange_item_name+' '+self.exchange_item_price
    

class Feedback(models.Model):
    name=models.CharField(max_length=32)
    email=models.CharField(max_length=64)
    phone=models.CharField(max_length=16)
    message=models.CharField(max_length=1000)
    
    
    
    