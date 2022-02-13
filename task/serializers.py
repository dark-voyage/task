from rest_framework import serializers
from .models import Ad, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['link', 'id']

class AdSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,)
    class Meta:
        model = Ad
        fields = ['name', 'price', 'images', 'id']
   


