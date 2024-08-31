from django.http import HttpResponse, JsonResponse
from .models import WatchList , StreamPlatform 
from .serializers import WatchListSerializers, StreamPlatformSerializer

# Create your views here. 

def movie_list(request):  
    movie_list = WatchList.objects.all() 
    serialized = WatchListSerializers(movie_list,many=True)

    return JsonResponse(serialized.data,safe=False)

def movie_detail(request,pk):  
    movie = WatchList.objects.get(pk=pk)  
    serialized = WatchListSerializers(movie)

    return JsonResponse(serialized.data)
