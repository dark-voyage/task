from urllib import request
from django.urls import path
from .views import AdsView, AdsListView
urlpatterns = [
    path('ads/', AdsListView.as_view()),
    path('ads/<int:pk>/', AdsView.as_view()),

]