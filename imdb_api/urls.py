from django.urls import path  
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns

streamplatform_list = views.StreamPlatformViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
streamplatform_detail = views.StreamPlatformViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
 
watchlist_view = views.WatchListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
watchlist_detail = views.WatchListViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})




urlpatterns = [
    path('list/',watchlist_view,name="watchlist_view"),
    path('list/<int:pk>',watchlist_detail,name="watchlist_detail"),
    path('stream/',streamplatform_list,name="streamplatform_list"),
    path('stream/<int:pk>',streamplatform_detail,name="streamplatform_detail"), 
    path('', views.api_root),

]
urlpatterns = format_suffix_patterns(urlpatterns)
