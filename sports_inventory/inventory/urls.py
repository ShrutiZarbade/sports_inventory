""" This File contains the inventory urls"""
from django.urls import path,include
from . views import InventoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', InventoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

