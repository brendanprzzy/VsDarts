# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 00:22:47 2017
Program used to keep track of score when playing darts
@author: Brendan Przywara
"""

player_one = input("Enter the name of player 1: ")
player_two = input("Enter the name of player 2: ")

player_one_score = 301
player_two_score = 301
current_round = 0
game_on = True

while game_on == True:
    current_round += 1
    player_one_reset_score = player_one_score
    player_two_reset_score = player_two_score
    
    
    player_one_round_points = input("How many points did " + player_one + \
                                    " score this round? ")
    player_one_round_points_int = int(player_one_round_points)
    player_two_round_points = input("How many points did " + player_two + \
                                    " score this round? ")
    player_two_round_points_int = int(player_two_round_points)
    
    
    player_one_score -= player_one_round_points_int
    if player_one_score < 0:
        player_one_score = player_one_reset_score
        print(player_one, "has gone over! Resetting score back to",\
              player_one_reset_score)
    print(player_one, "now has", player_one_score, "points")
    
    
    player_two_score -= player_two_round_points_int
    if player_two_score < 0:
        player_two_score = player_two_reset_score
        print(player_two, "has gone over! Resetting score back to",\
              player_two_reset_score)
    print(player_two, "now has", player_two_score, "points")
    
    
    if player_one_score == 0:
        print(player_one, "wins!")
        break
    if player_two_score == 0:
        print(player_two, "wins!")
        break
    