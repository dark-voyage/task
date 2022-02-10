from .models import Advertisement
from .serializers import AdSerializer
from rest_framework import mixins
from rest_framework import generics
class AdsListView(generics.ListCreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer


class AdsView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)