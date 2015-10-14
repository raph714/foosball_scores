from django.contrib import admin
from .models import Player, Game, ScoreChange
from django.db.models import Sum


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ['score',]
    list_display = ('name', 'score', 'wins', 'losses', 'total_games')

    def score(self, obj):
        return obj.score

    def total_games(self, obj):
        return obj.wins + obj.losses

admin.site.register(Player, PlayerAdmin)

class GameAdmin(admin.ModelAdmin):
    exclude = ['scores_calculated']
    list_display = ('date_created', 'team_a', 'team_b', 'team_a_score', 'team_b_score', 'team_changes')

    def save_related(self, request, form, formsets, change):
        super(GameAdmin, self).save_related(request, form, formsets, change)
        # game = form.instance
        # game.calculate_v2()
        for s in ScoreChange.objects.all():
            s.delete()

        for p in Player.objects.all():
            p.score = 1000
            p.wins = 0
            p.losses = 0
            p.save()

        for g in Game.objects.order_by('date_created',).all():
            g.scores_calculated = False
            g.save()
            g.calculate_v2()

    def team_a(self, obj):
        return ", ".join([p.name for p in obj.team_a_players.all()])

    def team_changes(self, obj):
        return ", ".join([s.__unicode__() for s in obj.score_changes.all()])

    def team_b(self, obj):
        return ", ".join([p.name for p in obj.team_b_players.all()])
        
admin.site.register(Game, GameAdmin)


class ScoreAdmin(admin.ModelAdmin):
    readonly_fields = ['player', 'change',]
    list_display = ['player', 'change',]
    ordering = ('game', )
admin.site.register(ScoreChange, ScoreAdmin)
