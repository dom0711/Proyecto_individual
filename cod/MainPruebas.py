# -*- coding: utf-8 -*-
"""
Main para hacer pruebas

@author: Dominick Rodríguez Trejos - B76600
"""

from Deck import Mazo
#interfaz en python takits

import pandas as pd

ruta_deck_propio = "C:\\Users\\usuar\\Desktop\\CA0305\\Proyecto_individual\\data\\deck_propio.xlsx"

def deck_creator(ruta_deck):
    base_deck = pd.read_excel(ruta_deck)
    deck_list = []
    for i in range(0, base_deck.shape[0]):
        carta = base_deck.loc[i, "Carta"]
        for j in range(0, base_deck.loc[i, "Cantidad"]):
            deck_list.append(carta)
    # Ahora tengo mi deck list completa, procedo a determinar cuales cartas son de cada utilidad
    starters = base_deck[base_deck["Utilidad"] == "Starter"]
    extenders = base_deck[base_deck["Utilidad"] == "Extender"]
    defensives = base_deck[base_deck["Utilidad"] == "Defensive"]
    combo_pieces = base_deck[base_deck["Utilidad"] == "Combo piece"]
    garnets = base_deck[base_deck["Utilidad"] == "Garnet"]
    non_engine = base_deck[base_deck["Utilidad"] == "Non engine"]
    # Y encuentro la cantidad que se tiene de cada utilidad
    num_starters = starters["Cantidad"].sum()
    num_extenders = extenders["Cantidad"].sum()
    num_defensives = defensives["Cantidad"].sum()
    num_combo_pieces = combo_pieces["Cantidad"].sum()
    num_garnets = garnets["Cantidad"].sum()
    num_non_engine = non_engine["Cantidad"].sum()
    # Por último creo la lista de valores iniciales para cuando resete el deck
    deck_inicial = [num_starters, num_extenders, num_defensives, num_combo_pieces, num_garnets, 
                    num_non_engine, deck_list, base_deck]
    # Finalmente puedo crear mi objeto tipo Mazo
    deck = Mazo(num_starters, num_extenders, num_defensives, num_combo_pieces, num_garnets, 
                num_non_engine, deck_list, base_deck, deck_inicial)
    return deck

deck_propio = deck_creator(ruta_deck_propio)

ruta_netdeck = "C:\\Users\\usuar\\Desktop\\CA0305\\Proyecto_individual\\data\\netdecked.xlsx"

netdeck = deck_creator(ruta_netdeck)


# hand_propio = deck_propio.hand_sample(5)
# hand_netdeck = netdeck.hand_sample(5)

# print("Mano propia: \n" f'{hand_propio}')
# print("Mano netdeck: \n" f'{hand_netdeck}')

# hand_propio_samples = []
# hand_netdeck_samples = []

# tourney_hands = deck_propio.tourney_sample()

# for i in range(0, 4):
#     print("Mano " f'{i + 1}' ": " f'{tourney_hands[i]}' "\n")

# print(hand_propio)
# print(deck_propio.rank_hand(hand_propio))


# deck_propio.reset_deck()

# total_scores = []
# for i in range(0, 25):
#     total_scores.append(deck_propio.eval_deck())
    
# print(total_scores)