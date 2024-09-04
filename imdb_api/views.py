from django.http import HttpResponse, JsonResponse
from .models import WatchList , StreamPlatform  
from .serializers import WatchListSerializer, StreamPlatformSerializer  
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.decorators import api_view 
from django.http import Http404 
from rest_framework.views import APIView 
from rest_framework import mixins
from rest_framework import generics 
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'WatchList': reverse('watch-list-view', request=request, format=format),
        'StreamPlatform': reverse('stream-platform', request=request, format=format)
    })


class WatchListView(generics.ListCreateAPIView): 
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer 

class WatchListDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer  

class StreamPlatformList(generics.ListCreateAPIView): 
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer 

class StreamPlatformDetails(generics.RetrieveUpdateDestroyAPIView): 
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer 

    

# class WatchListView(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView): 
#     queryset = WatchList.objects.all()
#     serializer_class = WatchListSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs) 
     
# class WatchListDetail(
#         mixins.RetrieveModelMixin,
#         mixins.UpdateModelMixin,
#         mixins.DestroyModelMixin,
#         generics.GenericAPIView ): 

#     queryset = WatchList.objects.all()
#     serializer_class = WatchListSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class StreamPlatformList(mixins.ListModelMixin,
#                        mixins.CreateModelMixin,
#                        generics.GenericAPIView): 
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
      

# class StreamPlatformDetails(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):  
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
 





         
















