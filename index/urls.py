from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='input'),
    path('success/', views.output, name='input'),
]
