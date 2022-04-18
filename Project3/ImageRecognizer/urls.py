from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('ch/', views.clear_history, name='clear_history'),
]