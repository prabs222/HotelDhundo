from django.db import models

# Create your models here.
class Amenities(models.Model):
    amenity = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.amenity

class Hotel(models.Model):
    class Ratings(models.IntegerChoices):
        POOR = 1
        AVERAGE = 2
        ORDINARY = 3
        GOOD = 4
        EXCELLENT = 5
    hotel_name = models.CharField(max_length=100)
    price = models.IntegerField()
    address = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    cover_image = models.ImageField(upload_to='cover_image')
    amenities = models.ManyToManyField(Amenities)
    rating = models.IntegerField(choices=Ratings.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.hotel_name
    
    def get_amenties(self):
        payload = []
        for amenity in self.amenities.all():
            payload.append({"id":amenity.id, "amenity":amenity.amenity})
        return payload
    
class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='hotel/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.hotel.hotel_name