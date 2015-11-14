from django.shortcuts import render
from django.views.generic import ListView
from .models import ScoreChange, Player, Game
from django.db.models import Q

# Create your views here.
class ScoresByPlayerDetail(ListView):

    model = Player

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ScoresByPlayerDetail, self).get_context_data(**kwargs)
        #Add the player score array by player to the context
        return context

class ScoresByPlayerCombinationDetail(ListView):
	template = '/foosball/player_combinations.html'
    model = Player

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        all_players = Player.objects.all();
        playerPairs = []
        for p1 in all_players:
        	for p2 in all_players:
        		if p1 != p2:
        			playerSet = set([p1, p2])
        			playerPairs.append(playerSet)

        gamesForPlayers = {}
        for playerSet in playerPairs:
        	games = Game.objects.filter(Q(team_a_players__in=playerSet) | Q(team_b_players__in=playerSet))
        	gamesForPlayers[playerSet] = games

        context['games'] = gamesForPlayers
        context = super(ScoresByPlayerCombinationDetail, self).get_context_data(**kwargs)
        #Add the player score array by player to the context
        return context