"""modul"""
from django.views.generic import ListView, DetailView

from .models import Advert


class AdvertPageView(ListView):
    """Вывод на странице Объявления"""
    model = Advert
    template_name = "adverts/adverts.html"
    context_object_name = 'adverts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оголошення'
        return context


class AdvertDetailView(DetailView):
    """Вывод детальной инф объявления"""
    model = Advert
    template_name = 'adverts/detail_advert.html'
    context_object_name = 'advert'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.subject
        return context