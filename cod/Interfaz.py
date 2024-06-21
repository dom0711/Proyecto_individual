# -*- coding: utf-8 -*-
"""
Interfaz

@author: Dominick Rodríguez Trejos - B76600

"""

# Para crear la inferfaz o app de nuestro proyecto vamos a utilizar la libreria Tkinter.
# La mayoría del código que se utiliza se construyo a base de tutoriales y guías en línea,
# pero principalmente las siguientes páginas web me ayudo mucho a entender como funcionan los widgets, 
# comandos y código de Tkinter:
    # https://realpython.com/python-gui-tkinter/
    # https://www.geeksforgeeks.org/python-tkinter-entry-widget/
# La idea será crear una ventana que muestre cuatro pestañas:
    # Crear Mazo: Desde aquí tenemos la opción de crear nuestro mazo desde un documento de Excel.
    # Calculadora Hipergeometrica: Desde aquí se pueden hacer las pruebas de consistencia del mazo.
    # Modo juego: Desde aquí se pueden simular manos, calificar las manos obtenidas y simular que 
    #             se toma una carta extra del mazo
    # Modo torneo: Desde aquí se pueden usar los métodos que usan el mazo completo, osea que no
    #              consideran que las cartas tomadas se devuelven al mazo, principalmente se puede
    #              crear las 45 manos del torneo, sacar una mano inicial y calificar el mazo 

# Primero importo los métodos del modulo Deck, y las librerias necesarias
from Deck import Mazo
import pandas as pd
import tkinter as tk

# Antes de empezar con la construcción de la interfaz tengo que preparar algunas funciones que 
# serán necesarias
# La idea inicial para ingresar decks era pedirle al usuario que ingrese el archivo del deck en 
# formato .YDK después de investigar me di cuenta que no iba a ser posible pues los archivos .YDK 
# lo que hacen en esencia es incluir el identificador de cada carta en formato txt, los simuladores 
# en linea lo que hacen es revisar los valore de cada identificador y relacionarlo directamente a 
# una carta y a sus valores, no tengo acceso a la base de datos de todas las cartas y además son más 
# de 10.000 cartas en el juego cada una con varios atributos y caracteristicas, y también no puede 
# entender como se formateaban los archivos .YDK.
#La segunda mejor opción me parece es pedirle al usuario que cargue un doc de Excel donde diga el
# nombre y utilidad de la carta y la cantidad

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

# Tras investigar un poco no logré que el objeto quedará guardado cuando se apreta el botón
# sospecho que la función si funciona pero como hace return se da un error pues no se guarda en
# ningún lado.
# Para resolver esto vamos a definir una variable, inicializada en Null llamada deck, y creo otra
# función que se encarge de ejecutar la función deck_creator() y guarde el mazo creado, esta misma
# idea se utiliza en el resto del código para diferentes variables que necesito crear y guardar.

# Entonces el método deck_creator() se ejecuta en la función guardar_deck() y esta se ejecuta
# cuando se presiona un botón, además se muestra un pop-up donde se confirme que el deck se creo
deck = None
def guardar_deck(ruta):
    global deck
    deck = deck_creator(ruta)
    tk.messagebox.showinfo("Confirmación", f''' Deck list: {deck.deck_list} 
            \n Cantidad de starters: {deck.starters} 
            \n Cantidad de extenders: {deck.extenders}
            \n Cantidad de cartas defensivas: {deck.defensives}
            \n Cantidad de piezas del combo: {deck.combo_pieces}
            \n Cantidad de Garnets: {deck.garnets}
            \n Cantidad de non engine: {deck.non_engine}
            \n Cantidad de cartas total: {len(deck.deck_list)}
            ''')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Ventana principal~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root = tk.Tk()
root.title("Deck Building Tool")
root.geometry("900x650")
# Para crear las pestañas lo puedo hacer con botones, estos botones una vez presionados cambian 
# lo que se ve en pantalla
# pestanas será el espacio donde se pondrán los botones, Frame() me permite crear el espacio 
# donde se pondrán los botones
pestanas = tk.Frame(root)
pestanas.pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pestañas~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Uso Frame() para crear el espacio donde voy a poner los botones y casillas de texto de cada 
# pestaña
tab_1_content = tk.Frame(root)
tab_2_content = tk.Frame(root)
tab_3_content = tk.Frame(root)
tab_4_content = tk.Frame(root)

# Creo la función que activa o desactiva las pestañas, en esencia lo que hace es cambiar lo que 
# aparece en la ventana cuando se presiona un botón
def show_tab(num_tab):
    '''
    Método que muestra la pestaña o botón seleccionado, este método se llama dentro de los botones
    que corresponden a las pestañas, así se muestra el contenido de la pestaña que se quiere ver.
    
    Parametros:
        num_tab: corresponde al número de la pestaña que se quiere ver, en cada botón de cada 
                 pestaña se le asigna el valor correspondiente a este parametro, tipo int
    '''
    tab_1_content.pack_forget()
    tab_2_content.pack_forget()
    tab_3_content.pack_forget()
    tab_4_content.pack_forget()

    if num_tab == 1:
        tab_1_content.pack(fill = tk.BOTH, expand = True)
    elif num_tab == 2:
        tab_2_content.pack(fill = tk.BOTH, expand = True)
    elif num_tab == 3:
        tab_3_content.pack(fill = tk.BOTH, expand = True)
    elif num_tab == 4:
        tab_4_content.pack(fill = tk.BOTH, expand = True)

# Creo los botones que funcionaran como pestañas
tab1_btn = tk.Button(pestanas, text = "Crear mazo", bg = "gray", fg = "black", 
                     font = ("Arial", 15), command = lambda: show_tab(1))
tab1_btn.pack(side = tk.LEFT, padx = 10, pady = 5)

tab2_btn = tk.Button(pestanas, text = "Calculadora Hipergeometrica", bg = "gray", fg = "black", 
                  font = ("Arial", 15), command = lambda: show_tab(2))
tab2_btn.pack(side = tk.LEFT, padx = 10, pady = 5)

tab3_btn = tk.Button(pestanas, text = "Modo juego", bg = "gray", fg = "black", 
                     font = ("Arial", 15), command = lambda: show_tab(3))
tab3_btn.pack(side = tk.LEFT, padx = 10, pady = 5)

tab4_btn = tk.Button(pestanas, text = "Modo torneo", bg = "gray", fg = "black", 
                     font = ("Arial", 15), command = lambda: show_tab(4))
tab4_btn.pack(side = tk.LEFT, padx = 10, pady = 5)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pestaña 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creo los botones y casillas de la pestaña 1:
    # 1 casilla para que el usuario inserte la ruta del doc de Excel donde tiene guardado los datos
    # de su deck
    # 1 botón para guardar la ruta
    # 1 botón para crear y guardar su mazo
    # 1 botón para mostrar el mazo
    
# Para acceder a lo que el usuario escribe dentro de la casilla se debe hacer con un botón 
# que guarde lo que el usuario escriba dentro de la casilla para luego usarlo, similar a como se
# hizo con el deck
ruta_deck = None
# Se crea el label que sirve como instrucción de lo que se debe insertar en la casilla
ins_ruta = tk.Label(tab_1_content, text = "Ingrese la ruta del mazo: ", font = ("Arial", 12))
ins_ruta.pack(side = tk.TOP, pady = 8)

# Se crea la casilla donde el usuario escribe la ruta del deck
cas_ruta = tk.Entry(tab_1_content, width = 80, font = ("Arial", 12), justify = tk.CENTER)
cas_ruta.pack(side = tk.TOP, pady = 8)

# Para guardar el texto se tiene que hacer con una función similar a como se hizo con el mazo.
def guardar_ruta_deck():
    global ruta_deck
    ruta_deck = cas_ruta.get()
    
# Ahora creo el botón que guarda la ruta
guardar_ruta_btn = tk.Button(tab_1_content, text = "Guardar", bg = "gray", fg = "black",
                              font = ("Arial", 12, "bold"), command = lambda: guardar_ruta_deck())
guardar_ruta_btn.pack(pady = 20)

# Por último creo el botón que se encarga de crear y guardar el deck
crear_deck_btn = tk.Button(tab_1_content, text = "Crear mazo", bg = "gray", fg = "black", 
                           font = ("Arial", 12, "bold"), command = lambda: guardar_deck(ruta_deck))
crear_deck_btn.pack(padx = 100, pady = 100)

# Creo la función que muestra el mazo, esta la voy a usar en todas las petañas
def show_deck():
    global deck
    tk.messagebox.showinfo("Confirmación", f''' Deck list: {deck.deck_list} 
            \n Cantidad de starters: {deck.starters} 
            \n Cantidad de extenders: {deck.extenders}
            \n Cantidad de cartas defensivas: {deck.defensives}
            \n Cantidad de piezas del combo: {deck.combo_pieces}
            \n Cantidad de Garnets: {deck.garnets}
            \n Cantidad de non engine: {deck.non_engine}
            \n Cantidad de cartas total: {len(deck.deck_list)}
            ''')

# Creo el botón para mostrar el deck en su estado actual
show_deck_tab_1_btn = tk.Button(tab_1_content, text = "Ver mazo", bg = "gray", fg = "black", 
                           font = ("Arial", 12, "bold"), command = lambda: show_deck())
show_deck_tab_1_btn.pack(pady = 20)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pestaña 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creo los botones y casillas de la pestaña 2:
    # 1 casilla donde el usuario pueda especificar la utilidad de la carta que desea tomar del deck
    # 1 casilla donde especifique la cantidad de copias de cartas de esa utilidad que desea tomar
    # 1 casilla donde especifique la cantidad de cartas que toma del mazo.
    # 1 botón que al presionarlo creé un pop-up donde se muestre la probabilidad de éxito
    # 1 casilla donde el usuario pueda indicar la cantidad de cartas que tomara del deck.
    # 1 botón que al presionarlo creé un pop-up donde se muestre la mano tomada.
    # 1 botón que al presionarlo creé un pop-up donde se muestre la calificación de la mano tomada.
    # 1 botón que le permita al usuario devolver al deck a su estado inicial.
    # Botones respectivos para cada casilla para guardar los valores insertados
    # 1 botón para mostrar el mazo
    
# Se sigue un formato muy similar al usado en la pestaña 1
# Creo la función que guarda la utilidad que el usuario escribe en la casilla
util = None
def guardar_util():
    '''
    Método que guardar la utilidad que el usuario escribe en la casilla
    
    '''
    global util
    util = cas_util.get()

# Creo el label que le indique al usuario lo que debe ingresar en la casilla
ins_util = tk.Label(tab_2_content, text = "Ingrese la utilidad deseada: ", font = ("Arial", 12))
ins_util.pack(side = tk.TOP, pady = 8)

# Creo la casilla donde el usuario ingresa la utilidad que se desea tomar del mazo
cas_util = tk.Entry(tab_2_content, width = 20, font = ("Arial", 12), justify = tk.CENTER)
cas_util.pack(side = tk.TOP, pady = 8)

# Creo el botón que guarda la utilidad ingresada
guardar_util_btn = tk.Button(tab_2_content, text = "Guardar", bg = "gray", fg = "black",
                              font = ("Arial", 12, "bold"), command = lambda: guardar_util())
guardar_util_btn.pack(pady = 10)

# Creo la función que guarda la cantidad de cartas a tomar del mazo
draw = None
def guardar_draw():
    global draw
    draw = int(cas_draw.get())

# Creo el label que le indique al usuario lo que debe ingresar en la casilla
ins_draw = tk.Label(tab_2_content, text = "Ingrese la cantidad de cartas a tomar: ", 
                    font = ("Arial", 12))
ins_draw.pack(side = tk.TOP, pady = 8)

# Creo la casilla donde el usuario ingresa la cantidad de cartas a tomar del mazo
cas_draw = tk.Entry(tab_2_content, width = 20, font = ("Arial", 12), justify = tk.CENTER)
cas_draw.pack(side = tk.TOP, pady = 8)

# Creo el botón que guarda la cantidad de cartas a tomar del mazo
guardar_draw_btn = tk.Button(tab_2_content, text = "Guardar", bg = "gray", fg = "black", 
                             font = ("Arial", 12, "bold"), command = lambda: guardar_draw())
guardar_draw_btn.pack(pady = 10)

# Creo la función que guarda la cantidad de cartas de esa utilidad que se desean
util_draw = None
def guardar_util_draw():
    global util_draw
    util_draw = int(cas_util_draw.get())

# Creo el label que le indique al usuario lo que debe ingresar en la casilla
ins_util_draw = tk.Label(tab_2_content, text = "Ingrese la cantidad de cartas que desea: ", 
                    font = ("Arial", 12))
ins_util_draw.pack(side = tk.TOP, pady = 8)

# Creo la casilla donde el usuario ingresa la cantidad de cartas de la utilidad que desea
cas_util_draw = tk.Entry(tab_2_content, width = 20, font = ("Arial", 12), justify = tk.CENTER)
cas_util_draw.pack(side = tk.TOP, pady = 8)

# Creo el botón que guarda la cantidad de cartas de la utilidad que desea
guardar_util_draw_btn = tk.Button(tab_2_content, text = "Guardar", bg = "gray", fg = "black",
                              command = lambda: guardar_util_draw(), font = ("Arial", 12, "bold"))
guardar_util_draw_btn.pack(pady = 20)

# Creo la función que aplique el método calc_hypergeom() y creé un pop-up con la probabilidad de
# éxito, luego el botón que lo ejecute
prob_exito = None
def show_prob_exito(util, util_draw, draw):
    global prob_exito
    prob_exito = deck.calc_hypergeom(util, util_draw, draw)
    tk.messagebox.showinfo("Probabilidad de exito", f'''{prob_exito}%''')

# Creo el botón que calcule la probabilidad de exito y la muestre en un pop-up
show_prob_exito_btn = tk.Button(tab_2_content, text = "Calcular probabilidad de éxito", 
                                  bg = "gray", fg = "black", font = ("Arial", 12, "bold"), 
                                  command = lambda: show_prob_exito(util, util_draw, draw))
show_prob_exito_btn.pack(pady = 20)

# Creo el botón para mostrar el deck en su estado actual
show_deck_tab_2_btn = tk.Button(tab_2_content, text = "Ver mazo", bg = "gray", fg = "black", 
                           font = ("Arial", 12, "bold"), command = lambda: show_deck())
show_deck_tab_2_btn.pack(pady = 20)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pestaña 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creo los botones y casillas de la pestaña 3:
    # 1 casilla donde el usuario pueda indicar cuantas cartas va a tomar del mazo para su mano.
    # 1 botón que le permite tomar la cantidad de cartas deseadas del mazo.
    # 1 botón que le permita calificar la mano que tomo.
    # 1 botón que le permita agregar una carta más a la mano
    # 1 botón que le permita resetear el mazo para empezar desde su estado inicial
    # Botones respectivos para cada casilla para guardar los valores insertados
    # 1 botón para mostrar el mazo

# Creo la función que guarda la cantidad de cartas que quiere tomar del mazo
draw_hand = None
def guardar_draw_hand():
    global draw_hand
    draw_hand = int(cas_draw_hand.get())
    
# Creo el label que le indique al usuario lo que debe ingresar en la casilla
ins_draw_hand = tk.Label(tab_3_content, text = "Ingrese la cantidad de cartas a tomar: ", 
                    font = ("Arial", 12))
ins_draw_hand.pack(side = tk.TOP, pady = 8)

# Creo la casilla donde el usuario ingresa la cantidad de cartas que quiere tomar
cas_draw_hand = tk.Entry(tab_3_content, width = 20, font = ("Arial", 12), justify = tk.CENTER)
cas_draw_hand.pack(side = tk.TOP, pady = 8)

# Creo el botón que guarda la cantidad de cartas a tomar del mazo
guardar_draw_hand_btn = tk.Button(tab_3_content, text = "Guardar", bg = "gray", fg = "black", 
                             font = ("Arial", 12, "bold"), command = lambda: guardar_draw_hand())
guardar_draw_hand_btn.pack(pady = 10)

# Defino la función que crea la mano y luego la enseña en un pop-up
hand_juego = None
def show_hand(draw_hand):
    global hand_juego
    hand_juego = deck.hand_sample(draw_hand)
    tk.messagebox.showinfo("Mano tomada", f'''{hand_juego}''')

# Creo el botón que toma y enseña la mano tomada
show_hand_btn = tk.Button(tab_3_content, text = "Mostrar mano", 
                                  bg = "gray", fg = "black", font = ("Arial", 12, "bold"), 
                                  command = lambda: show_hand(draw_hand))
show_hand_btn.pack(pady = 20)

# Creo la función que toma una carta del mazo y enseña la mano en un pop-up
def draw_one(hand):
    deck.draw_card(hand)
    tk.messagebox.showinfo("Mano", f'''{hand}''')

# Creo el botón para tomar una carta del mazo
draw_one_btn = tk.Button(tab_3_content, text = "Draw", bg = "gray", fg = "black", 
                         font = ("Arial", 12, "bold"), command = lambda: draw_one(hand_juego))
draw_one_btn.pack(pady = 20)

# Creo la función que califica la mano que se toma
score_hand = None
def show_score_hand(hand):
    global score_hand
    score_hand = deck.rank_hand(hand_juego)
    tk.messagebox.showinfo("Score", f'''Tu mano es una: {score_hand}''')
    
# Creo el botón para calificar la mano tomada
score_hand_btn = tk.Button(tab_3_content, text = "Calificar mano", bg = "gray", fg = "black",
                           font = ("Arial", 12, "bold"), 
                           command = lambda: show_score_hand(hand_juego))
score_hand_btn.pack(pady = 20)

# Creo la función que resetea el deck a su estado inicial
def reset_deck():
    global deck
    deck = deck_creator(ruta_deck)
    tk.messagebox.showinfo("Confirmación", "Mazo reseteado a su estado inicial")
    
# Creo el botón para resetear el mazo a su estado inicial
reset_deck_btn = tk.Button(tab_3_content, text = "Reset Deck", bg = "gray", fg = "black",
                           font = ("Arial", 12, "bold"), 
                           command = lambda: reset_deck())
reset_deck_btn.pack(pady = 20)

# Creo el botón que muestra el deck en su estado actual
show_deck_tab_3_btn = tk.Button(tab_3_content, text = "Ver mazo", bg = "gray", fg = "black", 
                           font = ("Arial", 12, "bold"), command = lambda: show_deck())
show_deck_tab_3_btn.pack(pady = 20)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Pestaña 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creo los botones y casillas de la pestaña 3:
    # 1 botón que le permita al usuario tomar una mano inicial del mazo.
    # 1 botón que le permita al usuario calificar la mano tomada
    # 1 botón que califique el deck del usuario
    
# Creo la función que toma una mano inicial del deck (5 cartas del deck en su estado inicial)
hand_torneo = None
def draw_sample_hand():
    '''
    Método que toma una mano inicial del mazo en su estado inicial
    
    Returns:
        Un pop-up con la mano inicial
    '''
    global hand_torneo
    hand_torneo = deck.starting_hand_sample()
    tk.messagebox.showinfo("Mano inicial", f'''{hand_torneo}''')

# Creo el botón que permite tomar una mano inicial y la muestra
show_draw_sample_hand_btn = tk.Button(tab_4_content, text = "Tomar mano inicial", bg = "gray", 
                                      fg = "black", font = ("Arial", 12, "bold"), 
                                      command = lambda: draw_sample_hand())
show_draw_sample_hand_btn.pack(pady = 40)
    
# Creo el botón para calificar la mano tomada, aquí voy a usar la función que creé en la pestaña 3
score_hand_sample_btn = tk.Button(tab_4_content, text = "Calificar mano", bg = "gray", fg = "black",
                           font = ("Arial", 12, "bold"), 
                           command = lambda: show_score_hand(hand_torneo))
score_hand_sample_btn.pack(pady = 40)

# Creo la función que va a evaluar el mazo
deck_score = None
def score_deck():
    '''
    Método que evalua el mazo
    
    Returns:
        Un pop-up con la calificación del mazo
    '''
    global deck_score
    deck_score = deck.eval_deck()
    tk.messagebox.showinfo("Clasificación del mazo", f'''{deck_score}''')
    
# Creo el botón para calificar el mazo
score_deck_btn = tk.Button(tab_4_content, text = "Calificar mazo", bg = "gray", fg = "black",
                           font = ("Arial", 12, "bold"), 
                           command = lambda: score_deck())
score_deck_btn.pack(pady = 40)


# Inicializo las petañas en la primera, la de creación de deck pues lo primero que se espera es que el
# usuario creé el deck y luego haga las pruebas
show_tab(1)

# Ejecutar el bucle principal de Tkinter, osea iniciar la aplicación
root.mainloop()

