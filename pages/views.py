# from django.shortcuts import render
from django.views.generic import TemplateView
from adverts.models import Advert
from services.models import Service


class HomePageView(TemplateView):
    template_name = "home.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'INFOpogreb'
        context['adverts'] = Advert.custom.moderation().order_by('-created')[:4]
        context['services'] = Service.custom_serv.moderation().order_by('-created')[:3]
        return context

