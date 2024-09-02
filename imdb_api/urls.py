from django.urls import path  
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('list',views.WatchListView.as_view(),name="watch-list-view"),
    path('list/<int:pk>',views.WatchListDetail.as_view(),name="watch-list-detail"),
    path('stream/',views.StreamPlatformList.as_view(),name="stream-platform"),
    path('stream/<int:pk>',views.StreamPlatformDetail.as_view(),name="stream-platform-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
