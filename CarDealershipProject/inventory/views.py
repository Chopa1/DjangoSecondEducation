# inventory/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ManufacturerForm, CarForm
from django.views.generic import TemplateView
from .models import Car, Manufacturer
from django.db.models import Avg, Max, Min


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'manufacturer_list.html'
    context_object_name = 'manufacturers'


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = 'manufacturer_detail.html'
    context_object_name = 'manufacturer'


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'manufacturer_form.html'
    success_url = reverse_lazy('manufacturer-list')


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'manufacturer_form.html'
    success_url = reverse_lazy('manufacturer-list')


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'manufacturer_confirm_delete.html'
    success_url = reverse_lazy('manufacturer-list')


class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('car-list')


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('car-list')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car-list')


class HomePageView(TemplateView):
    template_name = 'home.html'


class ReportView(TemplateView):
    template_name = 'report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Самая дорогая и самая дешевая машины
        context['most_expensive_car'] = Car.objects.order_by('-price').first()
        context['cheapest_car'] = Car.objects.order_by('price').first()

        # Средняя цена по маркам
        context['average_price_by_model'] = Car.objects.values('model').annotate(avg_price=Avg('price'))

        # Средняя цена по производителям
        context['average_price_by_manufacturer'] = Car.objects.values('manufacturer__name').annotate(
            avg_price=Avg('price'))

        return context