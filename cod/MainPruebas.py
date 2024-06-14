# -*- coding: utf-8 -*-
"""
Main para hacer pruebas

@author: Dominick Rodríguez Trejos - B76600
"""

from Deck import Mazo
#interfaz en python takits

import pandas as pd

ruta_deck_propio = "C:\\Users\\usuar\\Desktop\\CA0305\\Proyecto_individual\\data\\deck_propio.xlsx"
deck_propio_stats = pd.read_excel(ruta_deck_propio)

deck_propio_list = ["Effect Veiler", "Effect Veiler", "Effect Veiler","Jet Synchron", 
                    "Kurikara Divincarnate", "Rescue-ACE Hydrant", "Rescue-ACE Hydrant","Snake-Eye Ash", 
                    "Snake-Eye Oak", "Snake-Eyes Poplar", "Snake-Eyes Poplar", "Maxx C", "Maxx C", 
                    "Maxx C", "Ash Blossom & Joyous Spring", "Ash Blossom & Joyous Spring", 
                    "Ash Blossom & Joyous Spring", "Rescue-ACE Impulse", "Rescue-ACE Impulse", 
                    "Rescue-ACE Air Lifter", "Rescue-ACE Air Lifter", "Rescue-ACE Air Lifter", 
                    "Bystial Magnamhut", "Bystial Druiswurm", "Rescue-ACE Fire Attacker", 
                    "Bystial Baldrake", "Kashtira Fenrir", "Kashtira Unicorn", "Rescue-ACE Fire Engine", 
                    "Diabellstar the Black Witch", "Diabellstar the Black Witch", "Rescue-ACE Preventer",
                    "Rescue-ACE Preventer", "Snake-Eyes Flamberge Dragon", "Snake-Eyes Flamberge Dragon",
                    "Rescue-ACE Turbulence", "Rescue-ACE Turbulence", "Nibiru, the Primal Being", 
                    "Reinforcement of the Army", "Sinful Spoils of Subversion - Snake-Eye", 
                    "Bonfire", "Bonfire", "Bonfire", "Original Sinful Spoils - Snake-Eye", 
                    "Original Sinful Spoils - Snake-Eye", "Rescue-ACE HQ", 
                    "Pressured Plante Wraitsoth", "Divine Temple of the Snake-Eye", "Kashtira Birth", 
                    "Called by the Grave", "Called by the Grave", "Crossout Designator", "RESCUE!", 
                    "ALERT!", "EMERGENCY!", "EMERGENCY!", "EMERGENCY!", 
                    "WANTED: Seeket of Sinful Spoils", "CONTAIN!", "EXTINGUISH!"]

starters_propio = deck_propio_stats[deck_propio_stats["Utilidad"] == "Starter"]
extenders_propio = deck_propio_stats[deck_propio_stats["Utilidad"] == "Extender"]
defensives_propio = deck_propio_stats[deck_propio_stats["Utilidad"] == "Defensive"]
combo_pieces_propio = deck_propio_stats[deck_propio_stats["Utilidad"] == "Combo piece"]
garnets_propio = deck_propio_stats[deck_propio_stats["Utilidad"] == "Garnet"]
non_engine_propio = deck_propio_stats[deck_propio_stats["Utilidad"] == "Non engine"]


num_starters_propio = starters_propio["Cantidad"].sum()
num_extenders_propio = extenders_propio["Cantidad"].sum()
num_defensives_propio = defensives_propio["Cantidad"].sum()
num_combo_pieces_propio = combo_pieces_propio["Cantidad"].sum()
num_garnets_propio = garnets_propio["Cantidad"].sum()
num_non_engine_propio = non_engine_propio["Cantidad"].sum()

deck_propio_inicial = [num_starters_propio, num_extenders_propio,
                       num_defensives_propio, num_combo_pieces_propio, num_garnets_propio,
                       num_non_engine_propio, deck_propio_list, deck_propio_stats]

deck_propio = Mazo(num_starters_propio, num_extenders_propio, num_defensives_propio, 
                   num_combo_pieces_propio, num_garnets_propio, num_non_engine_propio, 
                   deck_propio_list, deck_propio_stats, deck_propio_inicial)

# ruta_netdeck = "C:\\Users\\usuar\\Desktop\\CA0305\\Proyecto_individual\\data\\netdecked.xlsx"
# netdeck_stats = pd.read_excel(ruta_netdeck)
# netdeck_list = ["Effect Veiler", "Effect Veiler", "Effect Veiler", "Rescue-ACE Hydrant", 
#                 "Rescue-ACE Hydrant", "Snake-Eyes Poplar", "Snake-Eyes Poplar", "Maxx C", "Maxx C",
#                 "Maxx C", "Ash Blossom & Joyous Spring", "Ash Blossom & Joyous Spring", 
#                 "Ash Blossom & Joyous Spring", "Rescue-ACE Impulse", "Rescue-ACE Impulse", 
#                 "Rescue-ACE Air Lifter", "Rescue-ACE Air Lifter", "Rescue-ACE Air Lifter", 
#                 "Rescue-ACE Fire Engine", "Diabellstar the Black Witch", "Diabellstar the Black Witch", 
#                 "Diabellstar the Black Witch", "Rescue-ACE Preventer", "Rescue-ACE Preventer",
#                 "Rescue-ACE Turbulence", "Bonfire", "Bonfire", "Bonfire", 
#                 "Original Sinful Spoils - Snake-Eye", "Original Sinful Spoils - Snake-Eye", 
#                 "Called by the Grave", "Called by the Grave", "RESCUE!", "ALERT!", "EMERGENCY!", 
#                 "EMERGENCY!", "EMERGENCY!", "WANTED: Seeket of Sinful Spoils", "CONTAIN!", 
#                 "EXTINGUISH!"]

# starters_netdeck = netdeck_stats[netdeck_stats["Utilidad"] == "Starter"]
# extenders_netdeck = netdeck_stats[netdeck_stats["Utilidad"] == "Extender"]
# defensives_netdeck = netdeck_stats[netdeck_stats["Utilidad"] == "Defensive"]
# combo_pieces_netdeck = netdeck_stats[netdeck_stats["Utilidad"] == "Combo piece"]
# garnets_netdeck = netdeck_stats[netdeck_stats["Utilidad"] == "Garnet"]
# non_engine_netdeck = netdeck_stats[netdeck_stats["Utilidad"] == "Non engine"]


# num_starters_netdeck = starters_netdeck["Cantidad"].sum()
# num_extenders_netdeck = extenders_netdeck["Cantidad"].sum()
# num_defensives_netdeck = defensives_netdeck["Cantidad"].sum()
# num_combo_pieces_netdeck = combo_pieces_netdeck["Cantidad"].sum()
# num_garnets_netdeck = garnets_netdeck["Cantidad"].sum()
# num_non_engine_netdeck = non_engine_netdeck["Cantidad"].sum()



# netdeck = Mazo(num_starters_netdeck, num_extenders_netdeck, num_defensives_netdeck, 
#                    num_combo_pieces_netdeck, num_garnets_netdeck, num_non_engine_netdeck, 
#                    netdeck_list, netdeck_stats)


hand_propio = deck_propio.hand_sample(5)
# hand_netdeck = netdeck.hand_sample(5)

# print("Mano propia: \n" f'{hand_propio}')
# print("Mano netdeck: \n" f'{hand_netdeck}')

# hand_propio_samples = []
# hand_netdeck_samples = []

# tourney_hands = deck_propio.tourney_sample()

# for i in range(0, 4):
#     print("Mano " f'{i + 1}' ": " f'{tourney_hands[i]}' "\n")

#score = deck_propio.rank_hand(hand_propio)


deck_propio.reset_deck()


