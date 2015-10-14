from django.db import models
from django.db.models import Sum


class Player(models.Model):
    name = models.CharField(max_length=200)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name

    @property
    def score(self):
        return ScoreChange.objects.filter(player=self).aggregate(Sum('change'))['change__sum'] + 1000


class ScoreChange(models.Model):
    player = models.ForeignKey(Player, related_name='score_changes')
    game = models.ForeignKey('foosball.Game', related_name='score_changes')
    change = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s:%s' % (self.player.name, self.change)


class Game(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    team_a_players = models.ManyToManyField(Player, related_name="team_a_games")
    team_b_players = models.ManyToManyField(Player, related_name="team_b_games")
    team_a_score = models.PositiveIntegerField(default=0)
    team_b_score = models.PositiveIntegerField(default=0)
    scores_calculated = models.BooleanField(default=False)

    def calculate_scores(self):
        if not self.scores_calculated:
            #calculate scores
            #get cumalative power rankings for each team
            team_a_power = 0
            for p in self.team_a_players.all():
                team_a_power = team_a_power + p.score

                #record the win/loss
                if self.team_a_score > self.team_b_score:
                    p.wins = p.wins + 1
                else:
                    p.losses = p.losses + 1
                p.save()

            team_b_power = 0
            for p in self.team_b_players.all():
                team_b_power = team_b_power + p.score

                #record the win/loss
                if self.team_a_score < self.team_b_score:
                    p.wins = p.wins + 1
                else:
                    p.losses = p.losses + 1
                p.save()

            if self.team_a_score > self.team_b_score:
                #calculate if team a won
                power_ratio = float(team_a_power) / float(team_b_power)
                score_ratio = float(self.team_a_score) - float(self.team_b_score)

                points = (score_ratio / power_ratio) * 10

                #now distribute the points from losers to winners.
                a1 = self.team_a_players.all()[0]
                a2 = self.team_a_players.all()[1]

                player_ratio = float(a1.score) / team_a_power
                a1_points = points * player_ratio
                a2_points = points - a1_points
                #give them their points
                a1.score = a1.score + a1_points
                a2.score = a2.score + a2_points
                a1.save()
                a2.save()

                #take the points from the losers
                b1 = self.team_b_players.all()[0]
                b2 = self.team_b_players.all()[1]

                player_ratio = float(b1.score) / team_b_power
                b1_points = points * player_ratio
                b2_points = points - b1_points
                #take their points
                b1.score = b1.score - b1_points
                b2.score = b2.score - b2_points
                b1.save()
                b2.save()
            else: 
                #calculate if team b won
                power_ratio = float(team_b_power) / float(team_a_power)
                score_ratio = float(self.team_b_score) - float(self.team_a_score)

                points = (score_ratio / power_ratio) * 10

                #now distribute the points from losers to winners.
                b1 = self.team_b_players.all()[0]
                b2 = self.team_b_players.all()[1]

                player_ratio = float(b1.score) / team_b_power
                b1_points = points * player_ratio
                b2_points = points - b1_points
                #give them their points
                b1.score = b1.score + b1_points
                b2.score = b2.score + b2_points
                b1.save()
                b2.save()

                #take the points from the losers
                a1 = self.team_a_players.all()[0]
                a2 = self.team_a_players.all()[1]

                player_ratio = float(a1.score) / team_a_power
                a1_points = points * player_ratio
                a2_points = points - a1_points
                #take their points
                a1.score = a1.score - a1_points
                a2.score = a2.score - a2_points
                a1.save()
                a2.save()

            #make sure it only happens once
            self.scores_calculated = True
            self.save()

    def calculate_v2(self):
        if not self.scores_calculated:
            #calculate scores
            #get cumalative power rankings for each team
            team_a_power = 0
            for p in self.team_a_players.all():
                team_a_power = team_a_power + p.score

                #record the win/loss
                if self.team_a_score > self.team_b_score:
                    p.wins = p.wins + 1
                else:
                    p.losses = p.losses + 1
                p.save()

            team_b_power = 0
            for p in self.team_b_players.all():
                team_b_power = team_b_power + p.score

                #record the win/loss
                if self.team_a_score < self.team_b_score:
                    p.wins = p.wins + 1
                else:
                    p.losses = p.losses + 1
                p.save()

            winners = self.team_a_players.all()
            losers = self.team_b_players.all()

            #calculate if team a won
            power_ratio = float(team_a_power) / float(team_b_power)
            score_ratio = float(self.team_a_score) - float(self.team_b_score)

            if self.team_a_score < self.team_b_score:
                winners = self.team_b_players.all()
                losers = self.team_a_players.all()
                
                #calculate if team a won
                power_ratio = float(team_b_power) / float(team_a_power)
                score_ratio = float(self.team_b_score) - float(self.team_a_score)
            

            points = (score_ratio / power_ratio) * 10

            #now add points to the winners
            pts_per_player = points / winners.count()
            for player in winners:
                score = ScoreChange(player=player, game=self, change=pts_per_player)
                score.save()

            #then take the points from the losers.
            pts_per_player = points / losers.count()
            for player in losers:
                score = ScoreChange(player=player, game=self, change=pts_per_player * -1)
                score.save()

            #make sure it only happens once
            self.scores_calculated = True
            self.save()

            