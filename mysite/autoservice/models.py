from datetime import date, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image
from tinymce.models import HTMLField
# import uuid
from user_profile.models import UserProfile


class CarModel(models.Model):
    brand = models.CharField(_('Brand'), max_length=30,
        help_text=_('ex.: Audi, BMW, FIAT...'))
    model = models.CharField(_('Model'), max_length=30)

    class Meta:
        ordering = ['brand']
        verbose_name = _('Car Model')
        verbose_name_plural = _('Cars Models')

    def __str__(self) -> str:
        return f'{self.brand} {self.model}'


class Car(models.Model):
    plate_no = models.CharField(_('Plate no'), max_length=6)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True, verbose_name=_('Car model'))
    vin_code = models.CharField(_('VIN code'), max_length=17)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, verbose_name=_('Client'))
    car_description = HTMLField(_('Car description'), max_length=10000, 
        help_text=_('Short car description'), blank=True, default='')

    
    picture = models.ImageField(_('Picture'), default='autoservice/img/default.png')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.picture.path)

    class Meta:
        ordering = ['plate_no']
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

    def __str__(self):
        return f'{self.car_model}'


class RepairOrder(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, verbose_name=_('Car'))
    sum = models.DecimalField(_('Sum'), max_digits=7, decimal_places=2, blank=True, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    due_back = models.DateField(_('Due back'), null=True, blank=True, db_index=True, default=date.today() + timedelta(days=7))

    LOAN_STATUS = (
        (0, _('New')),
        (10, _('Accepted')),
        (20, _('Under repair')),
        (30, _('Done')),
        (50, _('Returned')),
    )

    status = models.PositiveIntegerField(_('Status'), default=0, choices=LOAN_STATUS)

    class Meta:
        ordering = ['due_back']
        verbose_name = _('Repair order')
        verbose_name_plural = _('Repair orders')

    @property
    def is_overdue(self):
        if self.status < 50 and self.due_back and self.due_back < date.today():
            return True
        return False        

    def __str__(self):
        return f'{self.car}'


class Service(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    price = models.DecimalField(_('Price'), max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return f'{self.name} ({self.price} Eur)'
    

class OrderNo(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, verbose_name=_('Service'))
    remont_order = models.ForeignKey(RepairOrder, on_delete=models.CASCADE, null=True, verbose_name=_('Remont Order'), related_name='order_no') # reikia realaitedname prisikirti
    quantity = models.IntegerField(_('Quantity'))
    price = models.DecimalField(_('Price'), max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['remont_order']
        verbose_name = _('Repair job')
        verbose_name_plural = _('Repair jobs') 

    @property
    def repair_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f'{self.service} {self.price}'


class Comment(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, verbose_name=_('Client'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    for_order = models.ForeignKey(RepairOrder, null=True, blank=True, on_delete=models.CASCADE, related_name='comments', verbose_name=_('For order'))
    text = HTMLField(_('Comment'), max_length=10000, blank=True, default='')

    def __str__(self):
        return f'{self.created_at} - {self.text}'