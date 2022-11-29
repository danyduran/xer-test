from django.http import HttpResponse

from league.serializers import TeamSerializer, PlayerSerializer
from league.models import Team, Player
from rest_framework import viewsets


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
