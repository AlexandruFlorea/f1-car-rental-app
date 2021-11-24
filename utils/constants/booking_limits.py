from cars.models import Car


CAR_BOOKING_LIMIT = 5
TRACK_BOOKING_LIMIT = CAR_BOOKING_LIMIT * Car.objects.all().count()
