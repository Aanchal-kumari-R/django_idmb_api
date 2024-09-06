from rest_framework import serializers 
from .models import WatchList,StreamPlatform  

class WatchListSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = WatchList 
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):  
    watch_list = serializers.StringRelatedField(many=True,read_only=True) 
    class Meta:
        model = StreamPlatform  # Specify the model
        fields = '__all__'  # or list the specific fields you want to include 

        
