from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Car, CarModel, RepairOrder, Service, OrderNo, Comment



admin.site.site_header = _('Autoservice admin')
admin.site.site_title = _('Autoservice Admin')

class CarAdmin(admin.ModelAdmin):
    list_display = ('plate_no', 'car_model', 'vin_code', 'client')
    list_display_links = ('plate_no',)
    list_filter = ('client', 'car_model')
    search_fields = ('plate_no', 'vin_code')


class OrderNoAdmin(admin.ModelAdmin):
    list_display =  ('remont_order', 'service', 'price')


class RepairOrderAdmin(admin.ModelAdmin):
        list_display =  ('car', 'description', 'due_back', 'is_overdue')


class ServiceAdmin(admin.ModelAdmin):
    list_display =  ('name', 'price')


class CarModelAdmin(admin.ModelAdmin):
    list_display =  ('brand', 'model')

class CommentAdmin(admin.ModelAdmin):
    list_display =  ('created_at', 'text')


admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(RepairOrder, RepairOrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderNo, OrderNoAdmin)
admin.site.register(Comment, CommentAdmin)
