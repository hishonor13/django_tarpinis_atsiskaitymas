from datetime import date
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .models import Car, RepairOrder, Service, OrderNo


class CarListView(generic.ListView):
    model = Car
    template_name = 'autoservice/car_list.html'
    context_object_name = 'cars'
    queryset = Car.objects.all()
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'debug': settings.TIME_ZONE})
        return context


class RepairOrderView(generic.ListView):
    model = RepairOrder
    template_name = 'autoservice/order_list.html'
    context_object_name = 'orders'
    queryset = RepairOrder.objects.all()
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'debug': settings.TIME_ZONE})
        return context


class CarDetail(generic.DetailView):
    model = Car
    template_name = 'autoservice/car_detail.html'
    context_object_name = 'car'
    
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    # def form_valid(self, form):
    #     form.instance.car = self.object
    #     form.instance.client = self.request.user
    #     form.save()
    #     return super(CarDetail, self).form_valid(form)


class OrderDetail(generic.DetailView):
    model = RepairOrder
    template_name = 'autoservice/order_detail.html'
    context_object_name = 'order'
   


# Naujai kuriama
class CarRemontOrder(generic.CreateView, LoginRequiredMixin):
    model = RepairOrder
    fields = ['car', 'description']
    success_url = reverse_lazy('autoservice:cars')
    template_name = 'autoservice/create_order.html'







def index(request):
    num_cars = Car.objects.count()
    num_remont_orders = RepairOrder.objects.count()
    num_services = Service.objects.count()
    num_visits = int(request.session.get('num_visits', 0)) + 1
    request.session['num_visits'] = num_visits

    context = {
        'num_cars': num_cars,
        'num_remont_orders': num_remont_orders,
        'num_services': num_services,
        'num_visits': num_visits,

    }
    return render(request, 'autoservice/index.html', context=context)


def search_cars(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(
        Q(client__user__first_name__icontains=query) | 
        Q(client__user__last_name__icontains=query) | 
        Q(car_model__brand__icontains=query) | 
        Q(car_model__model__icontains=query) | 
        Q(plate_no__icontains=query) |
        Q(vin_code__icontains=query)
    )
    context = {
        'cars': search_results, 
        'query': query
    }
    return render(request, 'autoservice/search_cars.html', context=context)