import json
from users.models.details import Cart as CartModel


class Cart:
    def __init__(self, request):
        self._user = request.user
        self._data = request.session['cart'] if 'cart' in request.session else {}
        self._session = request.session

    def _save(self):
        self._session['cart'] = self._data

        if hasattr(self._user, 'cart'):
            self._user.cart.data = json.dumps(self._data)
            self._user.cart.save()
        else:
            CartModel.objects.create(user=self._user, data=json.dumps(self._data))

    def _clear(self):
        self._session['cart'] = {}

    # def add(self, *args, **kwargs):
    #     for arg in args:
    #         self._data[str(arg)] = str(arg)
    #         self._save()
    #
    # def remove(self, *args, **kwargs):
    #     for arg in args:
    #         del self._data[str(arg)]
    #         self._save()

    def add_car(self, car_id):
        self._data['car'] = car_id
        self._save()

    def remove_car(self):
        del self._data['car']
        self._save()

    def add_track(self, track_id):
        self._data['track'] = track_id
        self._save()

    def remove_track(self):
        del self._data['track']
        self._save()
