from rest_framework import serializers 
from .models import WatchList,StreamPlatform  ,Review

class WatchListSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = WatchList 
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):   
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model = Review 
        fields = '__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):  
    # watch_list = serializers.StringRelatedField(many=True,read_only=True)  
    watch_list = WatchListSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform  # Specify the model
        fields = '__all__'  # or list the specific fields you want to include 

        
    def validate_name(self,value): 
        if len(value)<=2: 
            raise serializers.ValidationError("Name is too short.") 
        return value   

    def validate(self, data): 
        if data['name'] == data['about']: 
            raise serializers.ValidationError("name and about should be different.") 
        return data 
