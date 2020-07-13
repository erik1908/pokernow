#!/usr/bin/env python

import sys
import os
import operator
import operator

players = {'patrick':73.54, 'Jardinero':61.97, 'Jeroen':0.17, 'Daan':-15.68, 'Castor':-20, 'Roger':-20, 'JONES':-80}

winners = {}
losers = {}
neutral = {}
final = {}


sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, ReportingCommand, Configuration, Option, validators


@Configuration()
class solvesplitter(ReportingCommand):
    """ %(synopsis)

    ##Syntax

    %(syntax)

    ##Description

    %(description)

    """


    def reduce(self, events):
        
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
               print(loser)

dispatch(solvesplitter, sys.argv, sys.stdin, sys.stdout, __name__)
