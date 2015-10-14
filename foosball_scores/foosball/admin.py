from django.contrib import admin
from .models import Player, Game


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ['score',]
    list_display = ('name', 'score', 'wins', 'losses')
admin.site.register(Player, PlayerAdmin)

class GameAdmin(admin.ModelAdmin):
    exclude = ['scores_calculated']
    list_display = ('date_created', 'team_a', 'team_b', 'team_a_score', 'team_b_score')

    def save_related(self, request, form, formsets, change):
        super(GameAdmin, self).save_related(request, form, formsets, change)
        game = form.instance
        game.calculate_scores()

    def team_a(self, obj):
        return ", ".join([p.name for p in obj.team_a_players.all()])

    def team_b(self, obj):
        return ", ".join([p.name for p in obj.team_b_players.all()])
        
admin.site.register(Game, GameAdmin)
