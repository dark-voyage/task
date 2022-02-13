from .models import Ad, Image
from .serializers import AdSerializer, ImageSerializer
from rest_framework import generics
from rest_framework import filters

class AdListView(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price', 'created_at']

class AdRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    def get_queryset(self):
        ad = Ad.objects.get(pk=self.kwargs.get('pk', None))
        images = Ad.objects.filter(ad=ad)
        return images