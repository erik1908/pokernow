from __future__ import division
from past.utils import old_div
import splunk.Intersplunk


import operator

def solveeq(text):
    players = {}
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
        return(k_winner, loser)

# get the previous search results
results,unused1,unused2 = splunk.Intersplunk.getOrganizedResults()
# for each results, add a 'shape' attribute, calculated from the raw event text
for result in results:
    result["loser"] = solveeq(result["_raw"])
# output results
splunk.Intersplunk.outputResults(results)