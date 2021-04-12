from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('help/', views.help_centre, name='help_centre')
]
