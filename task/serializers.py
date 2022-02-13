from rest_framework import serializers
from .models import Ad, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['link']

class AdSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,)
    
    class Meta:
        model = Ad
        fields = ['name', 'price', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        ad = Ad.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(ad=ad, **image_data)
        return ad


