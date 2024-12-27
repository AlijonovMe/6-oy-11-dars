from django.urls import path
from .views import *

urlpatterns = [
    # home
    path('', index, name='home'),

    # types
    path('type/<int:type_id>/', types, name='type_detail'),
    path('type/add/', addType, name='addType'),
    path('type/<int:type_id>/update', updateType, name='updateType'),
    path('type/<int:type_id>/delete', deleteType, name='deleteType'),

    # flowers
    path('flower/<int:flower_id>/', flower, name='flower_detail'),
    path('flower/add/', addFlower, name='addFlower'),
    path('flower/<int:flower_id>/update', updateFlower, name='updateFlower'),
    path('flower/<int:flower_id>/delete', deleteFlower, name='deleteFlower'),

    # auth
    path('auth/register/', register, name='register'),
    path('auth/login/', loginPage, name='login'),
    path('auth/logout/', logoutPage, name='logout'),
]
