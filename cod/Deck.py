# -*- coding: utf-8 -*-
"""
Modulo Deck

@author: Dominick Rodríguez Trejos - B76600
"""

class Mazo():
    
    # Constructor
    def __init__(self, starters, extenders, defensives, combo_pieces, garnets,
                 non_engine, deck_list, card_stats, deck_inicial):
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
            deck_inicial: contiene los atributos iniciales del Deck, se crea pensando en que en
                          algún momento se necesitará restablecer los atributos al estado inicial.
        
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
        self.__deck_inicial = [starters, extenders, defensives, combo_pieces, garnets, non_engine,
                               deck_list, card_stats]
        
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
    @property 
    def deck_inicial(self):
        return self.__deck_inicial
    
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
        
        Este método toma en cuenta que las cartas tomadas no se devuelven al deck, osea revisa
        cuales cartas se tomaron y actualiza los atributos del objeto, además permite usar en
        combinación con otros métodos que también consideran que las cartas tomadas no vuelven al
        mazo.
        
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
            # Reviso la utilidad de la carta tomada del mazo, esto lo hago en varios métodos.
            indice_draw = self.__card_stats.index[self.__card_stats["Carta"] == draw][0]
            if self.__card_stats.loc[indice_draw, "Utilidad"] == "Starter":
                self.__starters = self.__starters - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Extender":
                self.__extenders = self.__extenders - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Defensive":
                self.__defensives = self.__defensives - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Combo piece":
                self.__combo_pieces = self.__combo_pieces - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Garnet":
                self.__garnets = self.__garnets - 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Non engine":
                self.__non_engine = self.__non_engine - 1
        return mano
    
    def starting_hand_sample(self):
        '''
        Método que simula la primera mano que se toma del mazo, osea siempre toma 5 cartas del mazo
        similar al anterior pero este no considera que las cartas no vuelven al mazo, a nivel del código
        las cartas no se eliminan de la lista de cartas y los demás atributos del objeto no cambían,
        simplemente toma las cartas y las copia en una lista, a nivel físico es equivalente a tomar 5 
        cartas del mazo, devolverlas y revolver el mazo.
        
        Returns:
            starting_hand: las 5 cartas que toma del deck.
        '''
        mano = []
        import random
        import pandas
        for i in range(0, 5):
            draw = self.__deck_list[random.randint(0, len(self.__deck_list) - 1)]
            mano.append(draw)
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
        if self.__card_stats.loc[indice_draw, "Utilidad"] == "Starter":
            self.__starters = self.__starters - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Extender":
            self.__extenders = self.__extenders - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Defensive":
            self.__defensives = self.__defensives - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Combo piece":
            self.__combo_pieces = self.__combo_pieces - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Garnet":
            self.__garnets = self.__garnets - 1
        elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Non engine":
            self.__non_engine = self.__non_engine - 1
    
    def tourney_sample(self):
        '''
        Método que simula las 45 manos diferentes que se tomarían del mazo durante un 
        YCS(Yu-Gi-Oh! Championship Series), considerando más de 512 participantes, en total el ganador
        debería jugar un máximo de 15 partidos, cada una con un máximo de 3 duelos, pues el ganador es 
        el primero en ganar 2 duelos.
        Este método simula las 45 manos que tomaría el jugador y las califica.

        Returns
            total_hands: todas las manos que tomaría el jugador durante el torneo, tipo list.
        '''
        total_hands = []
        # Para la simulación de las 45 manos simplemente uso un for
        for i in range(0, 5):
            hand = self.starting_hand_sample()
            total_hands.append(hand)
        return total_hands
    
    def rank_hand(self, hand):
        '''
        Método que se encarga de asignarle una calificación a una mano que se toma del mazo

        Parametros:
            hand: se refiere a la mano que se tiene en este momento, tipo list.
            
        Returns:
            score: la calificación que se le asigna a la mano, tipo string
        '''
        # Con un for puedo revisar cada carta en la mano que se recibe
        # Para la calificación vamos primero a definir algunos principios:
          # 1. En la partida es fundamental lograr el combo de nuestro mazo, es lo más importante.
          # 2. Las cartas tienen una sola utilidad, osea solo pueden ser usadas una vez por turno.
          # 3. Asumimos que el jugador tiene la capacidad de completar el combo y usar sus cartas de
               # manera correcta.
        # 4. Hay cartas que no aportan nada al tomarlas del deck y en algunos casos incluso perjudican.
        # 5. Para calificar se debe entender que tan importante es cada tipo de carta
             # Starters: son las cartas más importantes del mazo, pues con ellas se puede lograr 
                          # el combo.
             # Extenders: son importantes pues si nuestros starters son negados o interrumpidos
                          # nos permiten continuar el combo.
             # Defensive: igual de importantes que los Starters, son cartas defensivas que ayudan
                          # a evitar el combo del oponente y evitan que nuestro oponente interrumpa el
                          # combo.
             # Combo piece: no aportan nada a la mano del inicio, ya que estás cartas las ibamos a
                          # obtener en algún momento durante el combo sin importar si las tomas del mazo
                          # desde un inicio.
             # Garnet: el termino Garnet se refiere a cartas que se deben incluir en el mazo por
                          # obligación, pero que nunca se quieren ver en la mano del inicio, perjudican.
             # Non engine: son cartas que no necesariamente ayudan a completar el combo, más bien
                          # lo complementan.
        # Vamos a guardar en una lista la utilidad de cada una de las cartas de la mano
        util_hand = []
        # Además, quiero guardar la cantidad de cada categoría que contiene la mano, entonces inicializo
        # en cero cada una y les voy agregando conforme revisa la mano.
        starters = 0
        extenders = 0
        defensives = 0
        combo_pieces = 0
        garnets = 0
        non_engine = 0
        for i in range(0, len(hand)):
            draw = hand[i]
            indice_draw = self.__card_stats.index[self.__card_stats["Carta"] == draw][0]
            if self.__card_stats.loc[indice_draw, "Utilidad"] == "Starter":
                util_hand.append("Starter")
                starters = starters + 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Extender":
                util_hand.append("Extender")
                extenders = extenders + 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Defensive":
                util_hand.append("Defensive")
                defensives = defensives + 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Combo piece":
                util_hand.append("Combo piece")
                combo_pieces = combo_pieces + 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Garnet":
                util_hand.append("Garnet")
                garnets = garnets + 1
            elif self.__card_stats.loc[indice_draw, "Utilidad"] == "Non engine":
                util_hand.append("Non engine")
                non_engine = non_engine + 1
        # Ahora tenemos una lista que incluye la utilidad de cada carta en la mano, tenemos que
        # determinar que tan buena es la mano.
        # Considerando las reglas del juego y los principios y valores que les dimos a cada categoría
        # podemos darnos una idea de cual sería la mejor mano posible, para esto definimos:
            # 1. A pesar de ser las cartas más importantes, tener más de una starter en la mano no es
            #    lo mejor, pues usualmente solo es posible usar un starter por turno
            # 2. Las cartas defensivas aportan mucho pues aseguran de que el combo se complete.
            # 3. En caso de que el starter sea interrumpido o que alguna parte del combo no se logre,
            #    un extender permite continuar el combo.
            # 4. El non-engine aporta muy poco al combo directamente, más que todo permite hacerlo un 
            #    poco más fuerte, entonces no es necesario tener estas cartas en la mano.
        # Con estas consideraciones podemos definir algunos rangos o categorias:
            # S+: Una mano que tiene 1 starter, 1 extender, 2 defensive, 1 non_engine
            # S: Una mano que tiene 1 starter, 1 extender, 1 defensive, y las otras dos cartas pueden
            #    ser cualesquiera, excepto garnets.
            # A: Una mano que tiene 1 starter, 0 extender, 1 defensive, y las otras tres pueden ser
            #    cualesquiera, excepto garnets.
            # B: Una mano que tiene 1 starter, 1 extender, 0 defensive, y las otras tres pueden ser
            #    cualesquiera, excepto garnets.
            # C: Una mano que tiene 1 starter, 0 extender, 0 defensive y las otras tres pueden ser
            #    cualesquiera, incluidas garnets.
            # D: Toda mano que no contenga un starter.
            # F: Toda mano que no contenga un starter y uno o más garnets.
        if garnets == 0:
            if starters == 0:
                return "D"
            else:
                if defensives == 0:
                    if extenders == 0:
                        return "C"
                    else:
                        return "B"
                else:
                    if extenders == 0:
                        return "A"
                    else:
                        return "S"
        else:
            if starters == 0:
                return "F"
            
        # if starters == 0:
        #     if garnets >= 2:
        #         return "F"
        #     else:
        #         return "D"
        # else:
        #     if (extenders == 0) and (defensives == 0):
        #         return "C"
        #     else:
        # elif (extenders == 1) and (defensives == 2) and (non_engine == 1):
        #     return "S"
        # elif (non_engine == 0) and (garnets == 0):
        #     if (extenders >= 1) and (defensives >= 1) and ()
        #     return "B"
        # elif 
        
    def calc_hypergeom(self, util_ideal, cant_deseo, cant_draw):
        '''
        Método que determina la probabilidad de tomar cant_ideal de cartas de una utilidad 
        especifica en una cantidad establecida de draws.
        
        Parametros:
            util_ideal: la utilidad de la carta que se desea tomar del deck, tipo string.
            cant_draw: la cantidad de cartas que toma del deck para intentar sacar la carta, tipo int
            cant_deseo: la cantidad de cartas de la utilidad uti_ideal que desea tomar del deck, 
                        tipo int
            
        Returns:
            prob_exito: la probabilidad de que saque una carta de la utilidad deseada, tipo float
        '''
        # La probabilidad de tomar una carta especifica del deck en una cantidad determinada de draws
        # se comporta como una distribución hipergeométrica, pues se toman cartas del deck y no se 
        # devuelven, entonces puedo calcular la probabilidad.
        # Considere P(X = j) = [(J, j) * (N - J, n - j)] / [(N, n)] donde los parentesis son
        # coeficientes binomiales y:
            # N: cantidad de cartas en el deck
            # J: cantidad de cartas con la utilidad deseada en el deck
            # n: cantidad de cartas que se toman del deck
            # j: cantidad de cartas de la utilidad deseada que se quieren sacar
        import math
        util_lower = util_ideal.lower()
        # Para obtener el atributo usando el parametro util_ideal y sin hacer un montón de ifs vamos a
        # usar el comando getattr(), se toma como base lo visto en el siguiente sitio web:
            # https://micro.recursospython.com/recursos/la-funcion-getattr.html
        # Además, voy a usar nombres cortos y sencillos para las variables porque la formula es larga.
        J = getattr(self, util_lower)
        j = cant_deseo
        N = len(self.__deck_list)
        n = cant_draw
        bino_1 = (math.factorial(J)) / ((math.factorial(j)) * (math.factorial(J - j)))
        bino_2 = (math.factorial(N - J)) / ((math.factorial(n - j)) * (math.factorial(N - J - n + j)))
        bino_3 = (math.factorial(N)) / ((math.factorial(n)) * (math.factorial(N - n)))
        prob_exito = (bino_1 * bino_2) / bino_3
        return prob_exito 
        
        
        
        