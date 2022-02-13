from rest_framework import serializers
from .models import Ad, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Ad
        fields = ['name', 'price', 'images']
    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('images')
    #     album = Ad.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Ad.objects.create(album=album, **track_data)
    #     return album
        


