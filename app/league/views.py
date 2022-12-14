from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from league.models import Player, Team
from league.serializers import PlayerSerializer, TeamSerializer
from rest_framework import viewsets


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "city"]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "goals", "team"]
