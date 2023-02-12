from django.shortcuts import render
from .models import *
from django.http import JsonResponse


# Create your views here.
def getHotels(request):
    try:
        hotels_obj = Hotel.objects.all()
        if request.GET.get("sort_by"):
            sort_by = request.GET.get("sort_by")
            if sort_by == "asc":
                hotels_obj = hotels_obj.order_by("price")
            elif sort_by == "desc":
                hotels_obj = hotels_obj.order_by("-price")
        if request.GET.get("amount"):
            sort_by_amount = request.GET.get("amount")
            hotels_obj = Hotel.objects.filter(price__lte=sort_by_amount)

        if request.GET.get("amenities"):
            amenities = str(request.GET.get("amenities")).split(",")
            # print(amenities)
            am = []
            for amenity in amenities:
                am.append(int(amenity))
            hotels_obj = hotels_obj.filter(amenities__in=am)
            # sort_by_amount = request.GET.get('amount')
            # hotels_obj = Hotel.objects.filter(price__lte = sort_by_amount)

        payload = []
        for obj in hotels_obj:
            payload.append(
                {
                    "hotel_name": obj.hotel_name,
                    "price": obj.price,
                    "address": obj.address,
                    "rating": obj.rating,
                    "cover_image": "/media/" + str(obj.cover_image),
                    "description": obj.description,
                    "amenities": obj.get_amenties(),
                }
            )

        return JsonResponse(payload, safe=False)

    except Exception as e:
        print(e)
        return JsonResponse({"message": str(e)})


def home(request):
    context = {"amenities": Amenities.objects.all()}
    return render(request, "home.html", context)
