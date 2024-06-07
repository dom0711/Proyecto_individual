# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:36:40 2024

@author: Usuario
"""

from Deck import Mazo

deck_list = ["Snake-Eye Ash", "Snake-Eye Ash", "Snake-Eye Ash", "Snake-Eyes Poplar",
             "Snake-Eye Oak", "Snake-Eye Birch", "Snake-Eyes Flamberge Dragon",
             "Diabellstar the Black Witch", "Rescue-ACE Hydrant", "Rescue-ACE Hydrant",
             "Rescue-ACE Hydrant", "Rescue-ACE Air Lifter", "Rescue-ACE Air Lifter", 
             "Rescue-ACE Impulse", "Rescue-ACE Impulse", "Rescue-ACE Impulse",
             "Rescue-ACE Fire Attacker", "Rescue-ACE Turbulence", "Rescue-ACE Turbulence",
             "Rescue-ACE HQ", "RESCUE!", "ALERT!", "CONTAIN!", "EXTINGUISH!", "REINFORCE!",
             "Original Sinful Spoils - Snake-Eye", "WANTED: Seeker of Sinful Sopils",
             "WANTED: Seeker of Sinful Sopils", "Called by the Grave", "Called by the Grave",
             "Infinite Impermanence", "Infinite Impermanence", "Infinite Impermanence", 
             "Maxx C", "Maxx C", "Maxx C", "Ash Blossom & Joyous Springs", 
             "Ash Blossom & Joyous Springs", "Ash Blossom & Joyous Springs", "Crossout Designator"]
deck_size = len(deck_list)
num_starters = 10
num_extenders = 4
num_defensives = 16
num_combo_pieces = 5
num_garnets = 5
num_non_engine = 0

deck = Mazo(num_starters, num_extenders, num_defensives, num_combo_pieces, num_garnets, 
            num_non_engine, deck_list, deck_size)

hand = deck.hand_sample(5)

deck.draw_card(deck.deck_list, hand)

