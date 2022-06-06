from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('description/', views.Description.as_view(), name="description"),
    path('watches/', views.WatchList.as_view(), name="watch_list")
]