from django.urls import path  
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('list',views.WatchListView.as_view(),name="watchlist-view"),
    path('list/<int:pk>',views.WatchListDetail.as_view(),name="watchlist-detail"),
    path('stream/',views.StreamPlatformList.as_view(),name="streamplatform"),
    path('stream/<int:pk>',views.StreamPlatformDetails.as_view(),name="streamplatform-detail"), 
    path('', views.api_root),

]


urlpatterns = format_suffix_patterns(urlpatterns)
