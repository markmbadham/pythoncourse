#!/usr/bin/env python
from random import randint
score = {}

def dice():
    return randint(1,6)

def setplayers(*players):
    for player in players:
        score[player] = 0
    
def turn():
    winner = None
    winning_roll = 0
    for player in score:
        raw_input('%s press key for dice roll' % player)
        roll = dice()
        print roll
        if roll > winning_roll: 
            winning_roll = roll
            winner = player

    score[winner] += 1 
    print "%s scores" % winner

def show_scores():
    print "SCORES"
    for player in score:
        print player, score[player]
    
