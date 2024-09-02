from django.http import HttpResponse, JsonResponse
from .models import WatchList , StreamPlatform  
from .serializers import WatchListSerializer, StreamPlatformSerializer  
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view 
from django.http import Http404 
from rest_framework.views import APIView



class WatchListView(APIView): 
    def get(self, request, format=None): 
        movie_list = WatchList.objects.all()
        serialized = WatchListSerializer(movie_list,many=True)
        return Response(serialized.data) 
    
    def post(self,request, format=None):  
        _data = request.data   
        serialized = WatchListSerializer(data =_data) 
        if serialized.is_valid(): 
            serialized.save() 
            return Response(serialized.data,status=status.HTTP_201_CREATED)  
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)

class WatchListDetail(APIView):  

    def get_object(self, pk):
        try:
            return WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):  
        watch_list = self.get_object(pk) 
        serializer = WatchListSerializer(watch_list) 
        return Response(serializer.data) 
    
    def put(self,request,pk,format=None):  
        watch_list = self.get_object(pk)
        serializer =  WatchListSerializer(watch_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None): 
        watch_list = self.get_object(pk)
        watch_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StreamPlatformList(APIView): 
    def get(self,request,format=None): 
        stream_list =  StreamPlatform.objects.all() 
        serialized = StreamPlatformSerializer(stream_list,many=True) 
        return Response(serialized.data)

    def post(self,request,format=None):  
        _data = request.data  
        serialized = StreamPlatformSerializer(data=_data)
        if serialized.is_valid():
             serialized.save() 
             return Response(serialized.data,status=status.HTTP_201_CREATED) 
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetail(APIView):
    """
    Retrieve, update or delete a StreamPlatform instance.
    """

    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stream_platform = self.get_object(pk)
        serializer = StreamPlatformSerializer(stream_platform)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stream_platform = self.get_object(pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stream_platform = self.get_object(pk)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 



         
















