from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.start),
    path('random', views.random),
    path('reset', views.reset),
]