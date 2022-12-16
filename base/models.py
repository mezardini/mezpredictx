from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Parameter(models.Model):
    home_name = models.CharField(max_length=50)
    home_goals = models.FloatField()
    home_conceded = models.FloatField()
    home_league_avg = models.FloatField()
    home_results = models.FloatField(null=True)
    away_name = models.CharField(max_length=50)
    away_goals = models.FloatField()
    away_conceded = models.FloatField()
    away_league_avg = models.FloatField()
    away_results = models.FloatField(null=True)
   
    over_three = models.FloatField(null=True)
    over_two = models.FloatField(null=True)
    home_resulsint = models.FloatField(null=True)
    away_resultsint = models.FloatField(null=True)
    overthreeint = models.FloatField(null=True)
    overtwoint = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = [ '-created']
    

    def __str__(self):
        return  self.home_name + " vs " + self.away_name


