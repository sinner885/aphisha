"""modul"""
from django.urls import path
from .views import ServicesListVeiw, ServiceDetailView, ServiceByCategoryListView

urlpatterns = [
 path("services/", ServicesListVeiw.as_view(), name="services"),
 path("services/<str:slug>/", ServiceDetailView.as_view(), name="detail_service"),
 path('category/<str:slug>/', ServiceByCategoryListView.as_view(), name="articles_by_category"),
]