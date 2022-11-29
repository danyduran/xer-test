from django.urls import include, path
from league import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"teams", views.TeamViewSet)
router.register(r"players", views.PlayerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", views.index, name="index"),
]
