# from django.http import HttpResponse, JsonResponse
from .models import WatchList , StreamPlatform  ,Review 
from .serializers import WatchListSerializer, StreamPlatformSerializer ,ReviewSerializer 
from rest_framework.response import Response 
from .permissions import AdminOrReadOnly,ReviewUserOrReadOnly
# from rest_framework import status 
from rest_framework.decorators import api_view 
# from django.http import Http404 
from rest_framework.views import APIView 
# from rest_framework import mixins
from rest_framework import generics 
from rest_framework.reverse import reverse 
from rest_framework import viewsets 
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated , IsAdminUser,IsAuthenticatedOrReadOnly


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'WatchList': reverse('watch-list-view', request=request, format=format),
        'StreamPlatform': reverse('stream-platform', request=request, format=format)
    })


class StreamPlatformViewSet(viewsets.ModelViewSet):  
      queryset = StreamPlatform.objects.all()
      serializer_class = StreamPlatformSerializer 


class WatchListViewSet(viewsets.ModelViewSet):  
     queryset = WatchList.objects.all()
     serializer_class = WatchListSerializer 
 
class ReviewCreate(generics.CreateAPIView):  
     #queryset = Review.objects.all()
     serializer_class = ReviewSerializer  
     #permission_classes = [ReviewUserOrReadOnly] 

     def get_queryset(self):
        return Review.objects.all() 


     def perform_create(self,serializer): 
          pk = self.kwargs['pk'] 
          movie = WatchList.objects.get(pk=pk)  
          review_user = self.request.user  
          review_queryset = Review.objects.filter(review_user = review_user , watchlist = movie)  
          if review_queryset.exists():  
               raise ValidationError("can't review multiple time.")


          serializer.save(watchlist=movie) 
          

class ReviewListView(generics.ListAPIView):  
     permission_classes = [AdminOrReadOnly]  
     queryset = Review.objects.all() 
     serializer_class = ReviewSerializer
     
     def get_queryset(self):
          pk = self.kwargs['pk'] 
          return Review.objects.filter(watchlist = pk)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):  
     # permission_classes = [IsAdminUser]
     permission_classes = [ReviewUserOrReadOnly]
     queryset = Review.objects.all() 
     serializer_class = ReviewSerializer




         
















