from rest_framework.decorators import api_view
from rest_framework.response import Response

from task.models import Advertisement
from task.serializers import AdSerializer

@api_view(['GET'])

def home(request):
    ads = Advertisement.objects.all()
    serializer = AdSerializer(ads, many=True)
    return Response(serializer.data)