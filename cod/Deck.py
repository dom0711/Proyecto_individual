# -*- coding: utf-8 -*-
"""
Modulo Deck

@author: Dominick Rodríguez Trejos - B76600

En este modulo se desarrolla la clase Deck y sus métodos
"""

import random
import math

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
        self.__deck_inicial = deck_inicial
        
    #Getters
    @property
    def starters(self):
        '''
        Método Get del atributo starters de la clase

        Returns:
            El atributo starters de la clase
        '''
        return self.__starters
    @property 
    def extenders(self):
        '''
        Método Get del atributo extenders de la clase

        Returns:
            El atributo extenders de la clase
        '''
        return self.__extenders
    @property 
    def defensives(self):
        '''
        Método Get del atributo defensives de la clase

        Returns:
            El atributo defensives de la clase
        '''
        return self.__defensives
    @property 
    def combo_pieces(self):
        '''
        Método Get del atributo combo_pieces de la clase

        Returns:
            El atributo combo_pieces de la clase
        '''
        return self.__combo_pieces
    @property 
    def garnets(self):
        '''
        Método Get del atributo garnets de la clase

        Returns:
            El atributo garnets de la clase
        '''
        return self.__garnets
    @property 
    def non_engine(self):
        '''
        Método Get del atributo non_engine de la clase

        Returns:
            El atributo non_engine de la clase
        '''
        return self.__non_engine
    @property 
    def deck_list(self):
        '''
        Método Get del atributo deck_list de la clase

        Returns:
            El atributo deck_list de la clase
        '''
        return self.__deck_list
    @property 
    def card_stats(self):
        '''
        Método Get del atributo card_stats de la clase

        Returns:
            El atributo card_stats de la clase
        '''
        return self.__card_stats
    @property 
    def deck_inicial(self):
        '''
        Método Get del atributo deck_inicial de la clase

        Returns:
            El atributo deck_inicial de la clase
        '''
        return self.__deck_inicial
    
    # Setters
    @starters.setter 
    def starters(self, starters):
        '''
        Método Set del atributo starters de la clase, asgina al atributo starters el valor starters

        Parametros:
            starters: corresponde al número de starters en el mazo, tipo int
        '''
        self.__starters = starters
    @extenders.setter 
    def extenders(self, extenders):
        '''
        Método Set del atributo extenders de la clase, asgina al atributo extenders el valor extenders

        Parametros:
            extenders: corresponde al número de extenders en el mazo, tipo int
        '''
        self.__extenders = extenders
    @defensives.setter 
    def defensives(self, defensives):
        '''
        Método Set del atributo defensives de la clase, asgina al atributo defensives el valor defensives

        Parametros:
            defensives: corresponde al número de defensives en el mazo, tipo int
        '''
        self.__defensives = defensives
    @combo_pieces.setter 
    def combo_pieces(self, combo_pieces):
        '''
        Método Set del atributo combo_pieces de la clase, asgina al atributo combo_pieces el valor 
        combo_pieces

        Parametros:
            combo_pieces: corresponde al número de combo_pieces en el mazo, tipo int
        '''
        self.__combo_pieces = combo_pieces
    @garnets.setter 
    def garnets(self, garnets):
        '''
        Método Set del atributo garnets de la clase, asgina al atributo garnets el valor garnets

        Parametros:
            garnets: corresponde al número de garnets en el mazo, tipo int
        '''
        self.__garnets = garnets
    @non_engine.setter 
    def non_engine(self, non_engine):
        '''
        Método Set del atributo non_engine de la clase, asgina al atributo non_engine el valor non_engine

        Parametros:
            non_engine: corresponde al número de non_engine en el mazo, tipo int
        '''
        self.__non_engine = non_engine
    @deck_list.setter 
    def deck_list(self, deck_list):
        '''
        Método Set del atributo deck_list de la clase, asgina al atributo deck_list el valor deck_list

        Parametros:
            deck_list: corresponde la lista de cartas del mazo, tipo list
        '''
        self.__deck_list = deck_list
    @card_stats.setter 
    def card_stats(self, card_stats):
        '''
        Método Set del atributo card_stats de la clase, asgina al atributo card_stats el valor card_stats

        Parametros:
            card_stats: corresponde al una base de datos que corresponde a la información de las carats del 
            mazo, tipo data frame de pandas
        '''
        self.__card_stats = card_stats
    @deck_inicial.setter 
    def deck_inicial(self, deck_inicial):
        '''
        Método Set del atributo deck_inicial de la clase, asgina al atributo deck_inicial el valor 
        deck_inicial

        Parametros:
            deck_inicial: corresponde a una lista que contiene la información del mazo en su estado inicial, 
            tipo list
        '''
        self.__deck_inicial = deck_inicial
    
    # Str
    def __str__(self):
        '''
        Método str de la clase
        
        Returns:
            Imprime los atributos del objeto en forma de string.
        '''
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
        # del deck - 1, uso el comando pop() porque cuando se toma una carta del deck se debe 
        # eliminar de las posibles cartas a tomar la próxima vez que se tome una carta del deck
        # Importar los paquetes al inicio
        import random
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
        for i in range(0, 5):
            draw = self.__deck_list[random.randint(0, len(self.__deck_list) - 1)]
            mano.append(draw)
        return mano
    
    def draw_card(self, mano):
        '''
        Método que agrega una carta a la mano de las cartas disponible en el deck
        
        Parametros:
            mano: se refiere a la mao que se tiene en el momento antes de tomar una carta 
                  más del deck, tipo list
        '''
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
        for i in range(0, 45):
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
            # S+: Una mano que tiene 1 starter, 1 extender, 1 defensive, 1 non_engine y la última carta
            #     puede ser cualquiera.
            # S: Una mano que tiene 1 starter, 1 extender, 1 defensive, 0 non_engine y las otras dos cartas
            #     pueden ser cualesquiera.
            # A: Una mano que tiene 1 starter, 0 extender, 1 defensive, y las otras tres pueden ser
            #    cualesquiera.
            # B: Una mano que tiene 1 starter, 1 extender, 0 defensive, y las otras tres pueden ser
            #    cualesquiera.
            # C: Una mano que tiene 1 starter, 0 extender, 0 defensive y las otras cuatro pueden ser
            #    cualesquiera.
            # D: Toda mano que no contenga un starter.
            # F: Toda mano que no contenga un starter y uno o más garnets.
        if starters >= 1:
            if non_engine >= 1:
                if defensives >= 1:
                    if extenders >= 1:
                        return "S+"
                    else:
                        return "A"
                else:
                    if extenders >= 1:
                        return "B"
                    else:
                        return "C"
            else:
                if defensives >= 1:
                    if extenders >= 1:
                        return "S"
                    else:
                        return "A"
                else:
                    if extenders >= 1:
                        return "B"
                    else:
                        return "C"
        else:
            if garnets >= 1:
                return "F"
            else:
                return "D"
        
    def calc_hypergeom(self, util_ideal, cant_deseo, cant_draw):
        '''
        Método que determina la probabilidad de tomar cant_ideal de cartas de una utilidad 
        especifica en una cantidad establecida de draws.
        
        Parametros:
            util_ideal: la utilidad de la carta que se desea tomar del deck, tipo string.
            cant_draw: la cantidad de cartas que toma del deck para intentar sacar la carta, 
                       tipo int
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
        util_lower = util_ideal.lower()
        # Para obtener el atributo usando el parametro util_ideal y sin hacer un montón de ifs 
        # vamos a usar el comando getattr(), se toma como base lo visto en el siguiente sitio web:
            # https://micro.recursospython.com/recursos/la-funcion-getattr.html
        # Además, voy a usar nombres cortos para las variables porque la formula es larga
        J = getattr(self, util_lower)
        j = cant_deseo
        N = len(self.__deck_list)
        n = cant_draw
        bino_1 = (math.factorial(J)) / ((math.factorial(j)) * (math.factorial(J - j)))
        bino_2 = (math.factorial(N - J)) / ((math.factorial(n - j)) * (math.factorial(N - J - n + j)))
        bino_3 = (math.factorial(N)) / ((math.factorial(n)) * (math.factorial(N - n)))
        prob_exito = (bino_1 * bino_2) / bino_3
        return prob_exito * 100
    
    def reset_deck(self):
        '''
        Método que reinicia el objeto a sus valores iniciales, util para cuando se quiere volver al
        estado inicial del deck.
        
        No hace returns ni recibe parametros, modifica los atributos del objeto con los que 
        se guardaron desde el inicio.
        '''
        self.__starters = self.__deck_inicial[0]
        self.__extenders = self.__deck_inicial[1]
        self.__defensives = self.__deck_inicial[2]
        self.__combo_pieces = self.__deck_inicial[3]
        self.__garnets = self.__deck_inicial[4]
        self.__non_engine = self.__deck_inicial[5]
        self.__deck_list = self.__deck_inicial[6]
        self.__card_stats = self.__deck_inicial[7]
        
    def eval_deck(self):
        '''
        Método que intenta evaluar el mazo basandose en el ranking que reciben las 45 posibles manos 
        que se tendrían que jugar en un YCS
        
        Considerando la naturaleza del juego es posible quedar eliminado del torneo con solamente 
        dos malas manos seguidas, la idea es que un mazo excelente nunca saca una mano que sea 
        peor a B, por lo que me interesa revisar el score minimo que se obtiene en 
        las 45 manos y ver cuantas veces se da este.

        Returns:
            deck_score: la calificación del deck, tipo string, en este caso se usaran solo cuatro:
                Tier 0: mazos que nunca tienen una mano peor o igual que B.
                Tier 1: mazos que tienen manos peores que o iguales a B, pero no tiene manos 
                        peores que B dos veces seguidas, osea puede que el mazo tenga malas manos 
                        pero nunca las tiene seguidas
                Tier 2: mazos que tienen manos peores que o iguales a B y tienen manos peores que B 
                        seguidas, osea el mazo tiene manos malas y puede tenerlas seguidas
                Tier 3: mazos que no tienen manos mejores que B, osea el mazo no saca buenas manos.
        '''
        # Primero reseteo el deck antes de empezar para asegurarme de estar tomando desde el deck inicial
        self.reset_deck()
        # Después obtengo las 45 manos con el método tourney_sample()
        total_manos = self.tourney_sample()
        score_manos_total = []
        # Reviso el score de cada mano y las guardo en una lista
        for mano in total_manos:
            score_manos_total.append(self.rank_hand(mano))
        # Ahora que tengo el score de las 45 manos podemos contar cuantas manos de cada tipo se obtienen y
        # dependiendo de la cantidad de manos peores a B se le asigna un tier.
        cant_S_plus = 0
        cant_S = 0
        cant_A = 0
        cant_B = 0 
        cant_C = 0 
        cant_D = 0 
        cant_F = 0 
        for score in score_manos_total:
            if score == "S+":
                cant_S_plus = cant_S_plus + 1 
            elif score == "S":
                cant_S = cant_S + 1
            elif score == "A":
                cant_A = cant_A + 1
            elif score == "B":
                cant_B = cant_B + 1
            elif score == "C":
                cant_C = cant_C + 1
            elif score == "D":
                cant_D = cant_D + 1
            elif score == "F":
                cant_F = cant_F + 1
        # Ahora tengo contandas la cantidad de cada tipo de mano que obtuvo en las 45, procedo a revisar si
        # el mazo solo produce manos malas osea peores que B, en ese caso solo puede ser Tier 3
        if (("B" not in score_manos_total) and ("A" not in score_manos_total) 
        and ("S" not in score_manos_total) and ("S+" not in score_manos_total)):
            return "Tier 3"
        # En caso que si produzca algunas manos buenas entonces se revisa si tiene manos malas, osea se
        # se revisa si nunca produce una mano C, D, F o B
        if (("B" not in score_manos_total) and ("C" not in score_manos_total) 
        and ("D" not in score_manos_total) and ("F" not in score_manos_total)):
            return "Tier 0"            
        # Si ninguno de los dos if anteriores devuelven un valor entonces se puede asumir que el mazo 
        # produce manos buenas y manos malas (caso usual), será Tier 1 o Tier 2, revisamos si produce manos
        # malas seguidas para determinar cual de los dos
        for i in range(0, len(score_manos_total)):
            # Solo nos importa si se repiten manos malas entonces reviso si la actual es una mala o buena
            if ((score_manos_total[i] == "C") or (score_manos_total[i] == "D") 
            or (score_manos_total[i] == "C")):
                # Revisamos si la siguiente también es mala, como es posible que la mano mala sea la última
                # entonces reviso que i no sea de manera que cause un index out of range
                if (i < len(score_manos_total) - 1):
                    if ((score_manos_total[i + 1] == "C") or (score_manos_total[i + 1] == "D") 
                    or (score_manos_total[i + 1] == "C")):
                        return "Tier 2"
        # Si se sale del for y no se devuelve el valor Tier 2 entonces el mazo debe ser Tier 1 entonces solo
        # hago el return al final afuera del for
        return "Tier 1"
                
                
        
        
        
        
        
        
        
        