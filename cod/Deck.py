# -*- coding: utf-8 -*-
"""
Modulo Deck

@author: Dominick Rodríguez Trejos - B76600
"""

class Mazo():
    
    # Constructor
    def __init__(self, starters, extenders, defensives, combo_pieces, garnets,
                 non_engine, deck_list, card_stats):
        '''
        Constructor del objeto Mazo, crea un objeto de tipo Mazo.
        
        Parametros:
            starters: se refiere al número de starters en el Deck, tipo int.
            extenders: se refiere al número de extenders en el Deck, tipo int.
            defensives: se refiere al número de cartas defensivas en el Deck, tipo int.
            combo_pieces: se refiere al número de piezas necesarias para el combo principal
                          en el Deck, tipo int.
            garnets: se refiere al número de garnets (cartas que queremos mantener en el Deck) 
                     en el Deck, tipo int.
            non_engine: se refiere al número de cartas que no corresponde a la base principal
                        del Deck en el Deck, tipo int.
            deck_list: se refiere a la lista de cartas en el Deck, tipo list.
            card_stats: se refiere a la base que contiene la utilidad de cada carta.
        
        Returns:
            Un objeto de tipo Mazo
        
        '''
        self.__starters = starters
        self.__extenders = extenders
        self.__defensives = defensives
        self.__combo_pieces = combo_pieces
        self.__garnets = garnets
        self.__non_engine = non_engine
        self.__deck_list = deck_list
        self.__card_stats = card_stats
        
    #Getters
    @property 
    def starters(self):
        return self.__starters
    @property 
    def extenders(self):
        return self.__extenders
    @property 
    def defensives(self):
        return self.__defensives
    @property 
    def combo_pieces(self):
        return self.__combo_pieces
    @property 
    def garnets(self):
        return self.__garnets
    @property 
    def non_engine(self):
        return self.__non_engine
    @property 
    def deck_list(self):
        return self.__deck_list
    @property 
    def card_stats(self):
        return self.__card_stats
    
    # Setters
    @starters.setter 
    def starters(self, starters):
        self.__starters = starters
    @extenders.setter 
    def extenders(self, extenders):
        self.__extenders = extenders
    @defensives.setter 
    def defensives(self, defensives):
        self.__defensives = defensives
    @combo_pieces.setter 
    def combo_pieces(self, combo_pieces):
        self.__combo_pieces = combo_pieces
    @garnets.setter 
    def garnets(self, garnets):
        self.__garnets = garnets
    @non_engine.setter 
    def non_engine(self, non_engine):
        self.__non_engine = non_engine
    @deck_list.setter 
    def deck_list(self, deck_list):
        self.__deck_list = deck_list
    @card_stats.setter 
    def card_stats(self, card_stats):
        self.__card_stats = card_stats
    
    # Str
    def __str__(self):
        return f''' Deck list: {self.__deck_list} 
                \n Cantidad de starters: {self.__starters} 
                \n Cantidad de extenders: {self.__extenders}
                \n Cantidad de cartas defensivas: {self.__defensives}
                \n Cantidad de piezas del combo: {self.__combo_pieces}
                \n Cantidad de Garnets: {self.__garnets}
                \n Cantidad de non engine: {self.__non_engine}
                \n Cantidad de cartas total: {len(self.__deck_list)}
                '''
    # Métodos
    def hand_sample(self, num_draw):
        '''
        Método que devuelve una mano del tamaño num_draw, usualmente 5, osea produce una 
        lista con las cartas que saca del deck de forma aleatoria cuando toma una cantidad
        de cartas del deck igual a num_draw.
        
        Parametros:
            num_draw: se refiere a la cantidad de cartas que se toman del deck, tipo int.
            
        Returns:
            mano: las cartas que toma aleatoriamente del deck, tipo list.
        '''
        # Creo una lista vacía, aquí pondré las cartas que toma aletoriamente del deck
        mano = []
        # Importo random para usar randint y así obtener un número aleatorio entre 0 y el tamaño
        # del deck - 1, uso el comando pop() porque cuando se toma una carta del deck se debe eliminar
        # de las posibles cartas a tomar la próxima vez que se tome una carta del deck
        import random
        import pandas as pd
        for i in range(0, num_draw):
            draw = self.__deck_list.pop(random.randint(0, len(self.__deck_list) - 1))
            mano.append(draw)
            indice_draw = self.__card_stats.index[self.__card_stats["Carta"] == draw][0]
            temp_starters = self.__starters
            temp_extenders = self.__extenders
            temp_defensives = self.__defensives
            temp_combo_pieces = self.__combo_pieces
            temp_garnets = self.__garnets
            temp_non_engine = self.__non_engine
            if self.__card_stats.loc[indice_draw, "Utilidad"] == "Starter":
                self.__starters = temp_starters - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Extender":
                self.__extenders = temp_extenders - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Defensive":
                self.__defensives = temp_defensives - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Combo piece":
                self.__combo_pieces = temp_combo_pieces - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Garnet":
                self.__garnets = temp_garnets - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Non engine":
                self.__non_engine = temp_non_engine - 1
        return mano
    
    def draw_card(self, deck, mano):
        '''
        Método que agrega una carta a la mano de las cartas disponible en el deck
        
        Parametros:
            deck: se refiere a las cartas que se tienen disponibles en el deck, tipo list
            mano: se refiere a la mao que se tiene en el momento antes de tomar una carta 
                  más del deck, tipo list
        '''
        import random
        draw = self.__deck_list.pop(random.randint(0, len(self.__deck_list) - 1))
        indice_draw = self.__card_stats.index[self.__card_stats["Carta"] == draw][0]
        mano.append(draw)
        temp_starters = self.__starters
        temp_extenders = self.__extenders
        temp_defensives = self.__defensives
        temp_combo_pieces = self.__combo_pieces
        temp_garnets = self.__garnets
        temp_non_engine = self.__non_engine
        if self.__card_stats.loc[indice_draw, "Utilidad"] == "Starter":
            self.__starters = temp_starters - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Extender":
            self.__extenders = temp_extenders - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Defensive":
            self.__defensives = temp_defensives - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Combo piece":
            self.__combo_pieces = temp_combo_pieces - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Garnet":
            self.__garnets = temp_garnets - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Non engine":
            self.__non_engine = temp_non_engine - 1
    
    def calc_hypergeom(self, uti_ideal, cant_ideal, cant_draw):
        '''
        Método que determina la probabilidad de tomar cant_ideal de cartas de una utilidad 
        especifica en una cantidad establecida de draws.
        
        Parametros:
            uti_ideal: la utilidad de la carta que se desea tomar del deck, tipo string.
            cant_draw: la cantidad de cartas que toma del deck para intentar sacar la carta, tipo int
            cant_ideal: la cantidad de cartas de la utilidad uti_ideal que desea tomar del deck, tipo int
            
        Returns:
            prob_exito: la probabilidad de que saque una carta de la utilidad deseada, tipo float
        '''
        # La probabilidad de tomar una carta especifica del deck en una cantidad determinada de draws
        # se comporta como una distribución hipergeométrica, pues se toman cartas del deck y no se 
        # devuelven, entonces puedo calcular la probabilidad.
        # Considere P(X = cant_ideal) = [(K, k) * (N - K, n-k)] / [(N, n)] donde los parentesis son
        # coeficientes binomiales y:
            # N: cantidad de cartas en el deck
            # K: cantidad de cartas con la utilidad deseada en el deck
            # n: cantidad de cartas que se toman del deck
            # k: cantidad de cartas de la utilidad deseada que se quieren sacar
        
        
        
        
        
        
        