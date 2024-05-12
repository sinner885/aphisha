"""modul"""
from django.urls import path
from .views import AdvertByCategoryListView, AdvertPageView, AdvertCreateView, \
            AdvertUpdateView, AdvertDeleteView, AdvertDetailView

urlpatterns = [
 path("adverts/", AdvertPageView.as_view(), name="adverts"),
 path("adverts/create", AdvertCreateView.as_view(), name="adverts_create"),
 path("adverts/<str:slug>/", AdvertDetailView.as_view(), name="detail_advert"),
 path('adverts/category/<str:slug>/', AdvertByCategoryListView.as_view(), name="adverts_by_category"),
 path("adverts/<str:slug>/update/", AdvertUpdateView.as_view(), name="advert_update"),
 path("adverts/<str:slug>/delete/", AdvertDeleteView.as_view(), name="advert_delete"),
]