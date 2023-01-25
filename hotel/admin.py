from django.contrib import admin
from .models import *
# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'price','address','rating']


admin.site.register(Amenities)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(HotelImage)
