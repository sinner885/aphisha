"""modul"""
from django.urls import path
from .views import AdvertPageView, AdvertDetailView

urlpatterns = [
 path("adverts/", AdvertPageView.as_view(), name="adverts"),
 path("adverts/<str:slug>/", AdvertDetailView.as_view(), name="detail_advert")
]