from django.contrib import admin
from django.utils.html import format_html
from my_admin.admin import my_admin_site
from cars.models import Car, Category


@admin.register(Car, site=my_admin_site)  # register on the custom admin site
class CarAdmin(admin.ModelAdmin):
    @staticmethod
    def team_color(obj):
        if obj.color:
            return format_html(
                f'<div style="width: 20px; height: 20px; border-radius: 50%; background-color: {obj.color};'
                f'border: 1px solid black;"></div>'
            )

        return 'N/A'

    team_color.short_description = 'team_color'
    team_color.admin_order_field = 'team_color'

    list_display = ['name', 'power_unit', 'races_won', 'handling', 'rate',
                    'available', 'category', 'team_color', 'number_of_bookings', 'number_of_active_bookings', 'owner']
    search_fields = ['name', 'power_unit', 'available', 'category__name', ]
    ordering = ['name', '-rate']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)  # accesses the parent queryset

        if request.user.is_superuser:
            return queryset

        return queryset.filter(owner=request.user)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)

        if not request.user.is_superuser:
            fields.remove('owner')

        return fields

    # save method overwriting is needed every time we change or add a new object
    def save_model(self, request, obj, form, change):
        if not obj.pk and not request.user.is_superuser:
            obj.owner = request.user  # auto add the owner

        return super().save_model(request, obj, form, change)


@admin.register(Category, site=my_admin_site)  # register on the custom admin site
class CategoryAdmin(admin.ModelAdmin):
    pass
