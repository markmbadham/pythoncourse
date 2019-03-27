'''
Created on 9 May 2018

@author: mark
'''
import random
import functions

DICE_MIN = 1
DICE_MAX = 6
PLAYERS = ['fred', 'thabo', 'nana']
TOTALS = [0] * len(PLAYERS)
def roll():
    return random.randint(DICE_MIN,DICE_MAX)

def turn():
    num_players = len(PLAYERS)
    score = [0]*num_players
    for player in range(num_players):
        score[player] = roll()
        print "player", PLAYERS[player], "scored", score[player]
    winning_score = max(score)
    print "Winning Score", winning_score
    
    for player in range(num_players):
        if score[player] == winning_score:
            TOTALS[player] += 1
            print "Player %s is a winner" % PLAYERS[player]

def endgame():
    max_total = max(TOTALS)
    print "Highest Total is", max_total 
    print functions.graph(TOTALS, PLAYERS)

def game(turns=5):
    print "STATRTING GAME of %d turns" % turns
    print "="*10
    for i in range(turns):
        print "turn %d" % i
        turn()
        print "-"*10
    endgame()
    
game()