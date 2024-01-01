#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Service, CategoryService

class ServicesListVeiw(ListView):
    '''список добавленых услуг'''
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services'
    paginate_by = 3

    def get_queryset(self):
        queryset = Service.custom_serv.moderation().order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Послуги'
        context['categorys'] = CategoryService.objects.all()
        return context


class ServiceDetailView(DetailView):
    '''вывод детельной инф. услуги'''
    model = Service
    template_name = 'services/detail_service.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['catgorys'] = CategoryService.objects.all()


class ServiceByCategoryListView(ListView):
    '''список услуг по категории'''
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'adverts'
    
    category = None

    def get_queryset(self):
        self.category = CategoryService.objects.get(slug=self.kwargs['slug'])
        queryset = Service.custom_serv.moderation().order_by('-created').filter(category__slug=self.category.slug)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Послуги категорії: {self.category.name}'
        context['categorys'] = CategoryService.objects.all()
        return context