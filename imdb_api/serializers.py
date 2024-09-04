from rest_framework import serializers 
from .models import WatchList,StreamPlatform  

class WatchListSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = WatchList 
        fields = '__all__'


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer): 
    url = serializers.HyperlinkedIdentityField(view_name="streamplatform-detail")
    class Meta:
        model = StreamPlatform  # Specify the model
        fields = '__all__'  # or list the specific fields you want to include 

        
