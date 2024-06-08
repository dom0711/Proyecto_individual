# -*- coding: utf-8 -*-
"""
Main para hacer pruebas

@author: Dominick Rodríguez Trejos - B76600
"""

from Deck import Mazo
#interfaz en python takits

import pandas as pd

deck_stats = pd.read_excel("C:\\Users\\usuar\\Desktop\\CA0305\\Proyecto_individual\\docs\\deck_propio.xlsx")
deck_list = ["Effect Veiler", "Effect Veiler", "Effect Veiler", "Rescue-ACE Hydrant", "Rescue-ACE Hydrant",
             "Snake-Eyes Poplar", "Snake-Eyes Poplar", "Maxx C", "Maxx C", "Maxx C", 
             "Ash Blossom & Joyous Springs", "Ash Blossom & Joyous Springs", "Ash Blossom & Joyous Springs",
             "Rescue-ACE Impulse", "Rescue-ACE Impulse", "Rescue-ACE Air Lifter", "Rescue-ACE Air Lifter",
             "Rescue-ACE Fire Attacker", "Rescue-ACE Fire Engine", "Diabellstar the Black Witch",
             "Diabellstar the Black Witch", "Rescue-ACE Preventer", "Rescue-ACE Preventer", 
             "Rescue-ACE Turbulunce", "Rescue-ACE Turbulunce", "Bonfire", "Bonfire", "Bonfire", 
             "Original Sinful Spoils - Snake-Eye", "Original Sinful Spoils - Snake-Eye", "Rescue-ACE HQ",
             "Called by the Grave", "Called by the Grave", "RESCUE!", "ALERT!", "EMERGENCY!", "EMERGENCY!",
             "EMERGENCY!", "WANTED: Seeker of Sinful Spoils", "CONTAIN!", "EXTINGUISH!", 
             "Sinful Spoils of Betrayal - Silvera"]
deck_size = len(deck_list)
num_starters = 12
num_extenders = 5
num_defensives = 13
num_combo_pieces = 6
num_garnets = 6
num_non_engine = 0

deck = Mazo(num_starters, num_extenders, num_defensives, num_combo_pieces, num_garnets, 
            num_non_engine, deck_list, deck_stats)

hand = deck.hand_sample(5)
print(hand)


deck.draw_card(deck.deck_list, hand)
print(hand)



