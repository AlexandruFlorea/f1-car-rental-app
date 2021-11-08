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

    def add(self, *args, **kwargs):
        quantity = 1
        for arg in args:
            self._data[str(arg)] = str(quantity)
            self._save()

    def remove(self, *args, **kwargs):
        for arg in args:
            del self._data[str(arg)]
            self._save()
