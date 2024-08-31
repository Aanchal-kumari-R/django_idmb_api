from rest_framework import serializers 
from .models import WatchList,StreamPlatform 

class WatchListSerializers(serializers.Serializer):  

    id = serializers.IntegerField(read_only=True)    
    title = serializers.CharField(max_length=100)
    storyLine = serializers.CharField(max_length=200) 
   # platform = serializers.ForeignKey(StreamPlatform,on_delete=serializers.CASCADE)  
    active = serializers.BooleanField(default=True) 
    created = serializers.DateTimeField()   

    def create(self, validated_data):
        """
        Create and return a new `WatchList` instance, given the validated data.
        """
        return WatchList.objects.create(**validated_data)   
    
    def update(self, instance, validated_data):
         """
         Update and return an existing `WatchList` instance, given the validated data.
         """
         instance.title = validated_data.get('title', instance.title)
         instance.storyLine = validated_data.get('storyLine', instance.storyLine)
         instance.active = validated_data.get('active', instance.active)
         instance.created = validated_data.get('created', instance.created)
         instance.save()
         return instance




class StreamPlatformSerializer(serializers.Serializer):   

    id = serializers.IntegerField(read_only=True)     
    name = serializers.CharField(max_length=100)
    about = serializers.CharField(max_length=200) 
    website = serializers.URLField(max_length=200)   
 
    def create(self, validated_data):
        """
        Create and return a new `StreamPlatform` instance, given the validated data.
        """
        return WatchList.objects.create(**validated_data)   

    def update(self, instance, validated_data):
         """
         Update and return an existing `StreamPlatform` instance, given the validated data.
         """
         instance.name = validated_data.get('name', instance.name)
         instance.about = validated_data.get('about', instance.about)
         instance.website = validated_data.get('website', instance.website)
         instance.save()
         return instance

 

