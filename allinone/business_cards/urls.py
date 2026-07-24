from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('core1', views.core1, name='core1'),
    path('core2', views.core2, name='core2'),
    path('core3', views.core3, name='core3'),
    path('core4', views.core4, name='core4'),
]