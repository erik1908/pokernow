import operator

#players = {'Castor':-10, 'Daan':22.58, 'Jardinero':101.24, 'Jeroen Do':-10, 'Jeroen':-60.83, 'MFJ':0.96, 'Rogier':-10, 'Wanders':-33.95}
players = {'Jardinero':6.52, 'Jeroen':21.33, 'Patrick':-7.85, 'Rogier':-20}
winners = {}
losers = {}
neutral = {}
final = {}

for k, v in players.items():
     if v > 0:
          winners[k] = v
     elif v == 0:
          neutral[k] = v
     else:
          losers[k] = v

x = 0

for k_winner, v_winner in winners.items():
     for k_loser, v_loser in losers.items():
          if (v_winner==0) or (v_loser==0):
               continue
          elif (abs(v_loser)<v_winner):
               final[x] = {k_winner:[k_loser,round(abs(v_loser),2)]}
               v_winner = v_winner - abs(v_loser)
               losers[k_loser] = 0
               winners[k_winner] = v_winner
               x = x + 1
          elif (abs(v_loser)>v_winner):
               v_loser = abs(v_loser) - v_winner
               final[x] = {k_winner:[k_loser,round(v_winner,2)]}
               losers[k_loser] = -1*v_loser
               winners[k_winner] = 0
               v_winner = 0
               x = x + 1
               continue
          else:
               continue

for k_winner, loser in final.items():
     print(k_winner, loser)