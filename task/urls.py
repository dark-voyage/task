from urllib import request
from django.urls import path
from .views import AdListView, ImageListView, AdRUDView, ImageRUDView


urlpatterns = [
    path('ads/', AdListView.as_view()),
    path('ads/<int:pk>/', AdRUDView.as_view()),
    path('ads/img/', ImageListView.as_view()),
    path('ads/img/<int:pk>/', ImageRUDView.as_view()),
]