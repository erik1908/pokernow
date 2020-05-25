#!/usr/bin/env python

import sys
import os
import operator

#players = {'Castor':-10, 'Daan':22.58, 'Jardinero':101.24, 'Jeroen Do':-10, 'Jeroen':-60.83, 'MFJ':0.96, 'Rogier':-10, 'Wanders':-33.95}
#players = {'Castor':-11.75, 'Jardinero':6.61, 'Jeroen':-2.43, 'Makkie':-5.58, 'Odi':1, 'PATRICK':-22.45, 'Rogier':25.78, 'Ruben':8.82}
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
    @Configuration()
    def map(self, events):
        # Put your streaming preop implementation here, or remove the map method,
        # if you have no need for a streaming preop
        pass

    def reduce(self, events):
        players = events
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
               yield(k_winner, loser)        # Put your reporting implementation

          pass

dispatch(solvesplitter, sys.argv, sys.stdin, sys.stdout, __name__)
