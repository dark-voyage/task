from urllib import request
from django.urls import path
from .views import AdsView, AdsListView, ImagesCreateView, ImagesView
urlpatterns = [
    path('ads/', AdsListView.as_view()),
    path('ads/<int:pk>/', AdsView.as_view()),
    path('ads/img/', ImagesCreateView.as_view()),
    path('ads/img/<int:pk>/', ImagesView.as_view()),
]