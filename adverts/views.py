"""modul"""
from django.views.generic import ListView, DetailView
# from django.shortcuts import render
from .models import Advert, Category


class AdvertPageView(ListView):
    """Вывод на странице Объявления"""
    model = Advert
    template_name = "adverts/adverts.html"
    context_object_name = 'adverts'
    paginate_by = 3

    def get_queryset(self):
        queryset = Advert.custom.moderation().order_by('-created')
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оголошення'
        context['categorys'] = Category.objects.all()
        #context['adverts'] = Advert.custom.moderation().order_by('-created')
        return context


class AdvertDetailView(DetailView):
    """Вывод детальной инф объявления"""
    model = Advert
    template_name = 'adverts/detail_advert.html'
    context_object_name = 'advert'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.subject
        context['categorys'] = Category.objects.all()
        return context




class AdvertByCategoryListView(ListView):
    model = Advert
    template_name = 'adverts/adverts.html'
    context_object_name = 'adverts'
    
    category = None

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Advert.custom.moderation().order_by('-created').filter(category__slug=self.category.slug)
        return queryset
       

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Оголошення категорії: {self.category.name}'
        context['categorys'] = Category.objects.all()
        return context


