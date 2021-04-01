from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('favorites/', views.view_favorites, name='view_favorites'),
    path('add/<item_id>/', views.add_to_favorites, name='add_to_favorites'),
]
