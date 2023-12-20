# from django.shortcuts import render
from django.views.generic import TemplateView
from adverts.models import Advert


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'INFOpogreb'
        context['adverts'] = Advert.custom.all()
        return context

