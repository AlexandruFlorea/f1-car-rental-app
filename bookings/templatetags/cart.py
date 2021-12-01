from django import template

register = template.Library()


# Custom filter tag to load in templates
@register.filter(name='dict_length')  # name of the filter to use in templates
def dict_length(parent, key):
    my_dict = parent.get(key, {})

    return len(my_dict.keys())


# tags can take multiple params and can have access to the context data from template
@register.simple_tag(name='cart_data')
def get_cart_data(parent, key):
    my_dict = parent.get(key, {})

    return len(my_dict.keys())


@register.inclusion_tag(filename='bookings/tags/cart.html', name='cart_link')
def get_cart_link(session):
    cart = session.get('cart', {})

    return {
        'items': len(cart.keys()),
    }
