from typing import List
from django.db import models
from django.db.models import Sum

# Create your models here.


class AuditModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(AuditModelMixin):
    name = models.CharField(max_length=255, blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.name} from {self.city}"

    @property
    def goals(self) -> int:
        total_goals = self.players.aggregate(Sum("goals"))
        return total_goals.get("goals__sum", 0)
    
    @property
    def players(self):
        return self.players.all()
    
    @property
    def player_names(self) -> List[str]:
        return [player.name for player in self.players.all()]


class Player(AuditModelMixin):
    name = models.CharField(max_length=255, blank=False, null=False)
    goals = models.PositiveSmallIntegerField(default=0)
    team = models.ForeignKey(
        Team, related_name="players", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name
