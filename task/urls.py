from urllib import request
from django.urls import path
from .views import AdListView, AdRUDView


urlpatterns = [
    path('ads/', AdListView.as_view()),
    # path('ads/<int:pk>/', AdRUDView.as_view()),
]