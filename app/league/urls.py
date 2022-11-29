from django.urls import path, include
from rest_framework import routers

from league import views


router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'players', views.PlayerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.index, name='index'),
]