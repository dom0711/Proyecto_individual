# -*- coding: utf-8 -*-
"""
Modulo Deck

@author: Dominick Rodríguez Trejos
"""

class Mazo():
    
    # Constructor
    def __init__(self, starters, extenders, defensives, combo_pieces, garnets,
                 non_engine, deck_list, deck_count):
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
            deck_count: se refiere a la cantidad de cartas en el Deck, tipo int.
        
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
        self.__deck_count = deck_count
        
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
    def deck_count(self):
        return self.__deck_count
    
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
    @deck_count.setter 
    def deck_count(self, deck_count):
        self.__deck_count = deck_count
    
    # Str
    def __str__(self):
        return f'''
                Deck list: {self.__deck_list} 
                \n Cantidad de starters: {self.__starters} 
                \n Cantidad de extenders: {self.__extenders}
                \n Cantidad de cartas defensivas: {self.__defensives}
                \n Cantidad de piezas del combo: {self.__combo_pieces}
                \n Cantidad de Garnets: {self.__garnets}
                \n Cantidad de non engine: {self.__non_engine}
                \n Cantidad de cartas total: {self.__deck_count}
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
        # Hago una copia del mazo, pues voy a tener que quitar elementos de la lista, ya que
        # cuando toma una carta del mazo esta se tiene que quitar de las posibles opciones
        # así no altero la lista original.
        deck_list_temp = self.__deck_list
        import random
        for i in range(0, num_draw):
            mano.append(deck_list_temp[random.randint(0, len(deck_list_temp) - 1)])
        return mano
    
        
        
        
        
        
        