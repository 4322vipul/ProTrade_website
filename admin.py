from django.contrib import admin
from .models import Items,ExchangeItems,Feedback

# Register your models here.
admin.site.register(Items)
admin.site.register(ExchangeItems)
admin.site.register(Feedback)