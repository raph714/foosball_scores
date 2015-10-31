from django.shortcuts import render
from django.views.generic import ListView
from .models import ScoreChange, Player, Game

# Create your views here.
class ScoresByPlayerDetail(ListView):

    model = Player

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ScoresByPlayerDetail, self).get_context_data(**kwargs)
        #Add the player score array by player to the context
        return context