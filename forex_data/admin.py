from django.contrib import admin
from .models import Price
# Register your models here.
class price_admin(admin.ModelAdmin):
    list_display = ['date', 'price']

admin.site.register(Price, price_admin)