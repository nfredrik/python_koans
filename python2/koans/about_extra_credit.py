#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

from runner.koan import *

from about_scoring_project import *   # roll
from about_dice_project import *  # DiceSet

class Player(object):
    def __init__(self, name):
        self._name = name
        self._score = 0
        
    def save_score(self,score):
        self._score += score
    
    def reached_win_score(self):
        return  self._score >= 3000
    
    def get_score(self):
        return self._score

    def get_name(self):
        return self._name
    
class Greeds(object):
    def __init__(self, diceset = None):
        self.diceset = diceset
        self.result = None
        self.no_of_rolls = 0
        
    def play(self):
        #print self.diceset.roll(5)
        self.result = score(self.diceset.roll(5))
        return self.result


import itertools

                        
players = [Player("Janne"), Player("Olle")]
cycle = itertools.cycle(players)

  
def get_cycle():

    global cycle
    return cycle.next()
    

class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        #self.assertTrue(False)  # This should be true

        nisse = Player("Nisse")
        nisse.save_score(300)
        
        self.assertEqual(False, nisse.reached_win_score())
    
        nisse.save_score(3000)
        self.assertEqual(True, nisse.reached_win_score())
        
        #self.assertTrue(False)  # This should be true
        
        dice_set = DiceSet()
        greed = Greeds(dice_set)
        
        self.assertEqual(int, type(greed.play()))
  

        
        janne = Player("Janne")
        dice = DiceSet()
        greed = Greeds(dice)
        
        count = 0
        
        while True:
            
            player = get_cycle()
            if player.reached_win_score():
                print "We reached our goal"
                break
            
            player.save_score(greed.play())
            count+=1
            #print janne.get_score()
            
        print "count:", count
        
        for player in players:
            print "player:", player.get_name(), "score:", player.get_score()                     
            