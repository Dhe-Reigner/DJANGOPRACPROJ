from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='my_index'),
    path('join/', views.join,name='my_join')
  
]
