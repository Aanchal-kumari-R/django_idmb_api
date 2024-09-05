from django.urls import path  , include
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns 
from rest_framework.routers import DefaultRouter


# Create a router and register our ViewSets with it.
router = DefaultRouter()  
router.register(r'stream', views.StreamPlatformViewSet, basename='streamplatform')
router.register(r'list', views.WatchListViewSet, basename='watchlist')


urlpatterns = [ 
    path('',include(router.urls)),
    path('',include(router.urls)),
    path('', views.api_root),

]
#urlpatterns = format_suffix_patterns(urlpatterns)
