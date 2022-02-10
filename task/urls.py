from urllib import request
from django.urls import path
from .views import AdView, AdListView, ImageCreateView, ImageView


urlpatterns = [
    path('ads/', AdListView.as_view()),
    path('ads/<int:pk>/', AdView.as_view()),
    path('ads/img/', ImageCreateView.as_view()),
    path('ads/img/<int:pk>/', ImageView.as_view()),
]