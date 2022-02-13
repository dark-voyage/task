from .models import Ad, Image
from .serializers import AdSerializer, ImageSerializer
from rest_framework import generics
from rest_framework import filters

class AdListView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [filters.OrderingFilter   ]
    ordering_fields = ['price', 'created_at']

class AdRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all() 
    serializer_class = AdSerializer

class ImageListView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer