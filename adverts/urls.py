"""modul"""
from django.urls import path
from .views import AdvertPageView, AdvertDetailView, AdvertByCategoryListView

urlpatterns = [
 path("adverts/", AdvertPageView.as_view(), name="adverts"),
 path("adverts/<str:slug>/", AdvertDetailView.as_view(), name="detail_advert"),
 path('category/<str:slug>/', AdvertByCategoryListView.as_view(), name="articles_by_category"),
]