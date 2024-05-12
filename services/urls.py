"""modul"""
from django.urls import path
from .views import ServicesListVeiw, ServiceDetailView, ServiceByCategoryListView, \
    ServiceCreateView, ServiceDeleteView, ServiceUpdateView

urlpatterns = [
 path("services/", ServicesListVeiw.as_view(), name="services"),
 path("services/create", ServiceCreateView.as_view(), name="service_create"),
 path("services/<str:slug>/", ServiceDetailView.as_view(), name="detail_service"),
 path('services/category/<str:slug>/', ServiceByCategoryListView.as_view(), name="servece_by_category"),
 path("services/<str:slug>/update/", ServiceUpdateView.as_view(), name="service_update"),
 path("services/<str:slug>/delete/", ServiceDeleteView.as_view(), name="service_delete"),
]