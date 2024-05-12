#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Service, CategoryService
from .forms import ServiceCreateForm

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
        context['categorys'] = CategoryService.objects.all()


class ServiceByCategoryListView(ListView):
    '''список услуг по категории'''
    model = Service
    template_name = 'services/services.html'
    context_object_name = 'services'
    
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


class ServiceCreateView(CreateView):
    """
    Представление: создание объявлений на сайте
    """
    model = Service
    template_name = 'services/service_create.html'
    form_class = ServiceCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавлення послуги'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ServiceUpdateView(UpdateView):
    """
    Представление: обновления материала на сайте
    """
    model = Service
    template_name = 'services/service_update.html'
    context_object_name = 'service'
    form_class = ServiceCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Оновлення послуги: {self.object.subject}'
        return context

    def form_valid(self, form):
        form.instance.updater = self.request.user
        form.save()
        return super().form_valid(form)


class ServiceDeleteView(DeleteView):
    """
    Представление: удаления материала
    """
    model = Service
    success_url = reverse_lazy('services')
    context_object_name = 'service'
    template_name = 'services/service_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Видалення оголошення: {self.object.subject}'
        return context