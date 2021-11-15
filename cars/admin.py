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
                f'<div style="width: 20px; height: 20px; border-radius: 50%; background-color: {obj.color}; border: 1px solid black;"></div>'
            )

        return 'N/A'

    team_color.short_description = 'team_color'
    team_color.admin_order_field = 'team_color'

    list_display = ['name', 'power_unit', 'races_won', 'handling', 'rate', 'available', 'category', 'team_color']
    search_fields = ['name', 'power_unit', 'available', 'category__name', ]
    ordering = ['name', '-rate']


@admin.register(Category, site=my_admin_site)  # register on the custom admin site
class CategoryAdmin(admin.ModelAdmin):
    pass
