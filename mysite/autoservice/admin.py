from django.contrib import admin
from .models import Car, CarModel, RepairOrder, Service, OrderNo


admin.site.site_header = "Autoserviso administravimas"

class CarAdmin(admin.ModelAdmin):
    list_display = ('plate_no', 'car_model', 'vin_code', 'client')
    list_display_links = ('plate_no',)
    list_filter = ('client', 'car_model')
    search_fields = ('plate_no', 'vin_code')


class OrderNoAdmin(admin.ModelAdmin):
    list_display =  ('remont_order', 'service', 'price')


class RepairOrderAdmin(admin.ModelAdmin):
        list_display =  ('car', 'description')


class ServiceAdmin(admin.ModelAdmin):
    list_display =  ('name', 'price')


class CarModelAdmin(admin.ModelAdmin):
    list_display =  ('brand', 'model')


admin.site.register(Car, CarAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(RepairOrder, RepairOrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderNo, OrderNoAdmin)
