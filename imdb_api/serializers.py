from rest_framework import serializers 
from .models import WatchList,StreamPlatform  

class WatchListSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = WatchList 
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform  # Specify the model
        fields = '__all__'  # or list the specific fields you want to include 

        
# class StreamPlatformSerializer(serializers.Serializer):   

#     id = serializers.IntegerField(read_only=True)     
#     name = serializers.CharField(max_length=100)
#     about = serializers.CharField(max_length=200) 
#     website = serializers.URLField(max_length=200)   
 
#     def create(self, validated_data):
#         """
#         Create and return a new `StreamPlatform` instance, given the validated data.
#         """
#         return WatchList.objects.create(**validated_data)   

#     def update(self, instance, validated_data):
#          """
#          Update and return an existing `StreamPlatform` instance, given the validated data.
#          """
#          instance.name = validated_data.get('name', instance.name)
#          instance.about = validated_data.get('about', instance.about)
#          instance.website = validated_data.get('website', instance.website)
#          instance.save()
#          return instance

 

