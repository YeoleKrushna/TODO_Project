
from django.contrib import admin
from django.urls import path,include
from todo import views
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
router = DefaultRouter()
router.register(r'todos',TodoViewSet)

urlpatterns = [
    
    path('',include(router.urls))
]
