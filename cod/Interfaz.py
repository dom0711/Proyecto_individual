# -*- coding: utf-8 -*-
"""
Interfaz

@author: Dominick Rodríguez Trejos - B76600

"""

# Para crear la inferfaz o app de nuestro proyecto vamos a utilizar la libreria Tkinter.
# La idea será crear una ventana que muestre dos pestañas:
    # Crear Mazo: Desde aquí tenemos la opción de crear nuestro mazo desde un documento de Excel.
    # Calculadora Hipergeometrica: Desde aquí se pueden hacer las pruebas de consistencia del mazo.
    # Modo juego: Desde aquí se pueden simular manos, calificar las manos obtenidas, simular las manos de un YCS
    #             y evaluar el mazo

# Primero importo los métodos del modulo Deck, y las librerias necesarias
from Deck import Mazo
import pandas as pd
from tkinter import *

# Antes de empezar con la construcción de la interfaz tengo que preparar algunas funciones que serán 
# serán necesarias
# La idea inicial para ingresar decks era pedirle al usuario que ingrese el archivo del deck en formato .YDK
# después de investigar me di cuenta que no iba a ser posible pues los archivos .YDK lo que hacen en esencia
# es incluir el identificador de cada carta en formato txt, los simuladores en linea lo que hacen es revisar
# los valore de cada identificador y relacionarlo directamente a una carta y a sus valores, no tengo acceso
# a la base de datos de todas las cartas y además son más de 10.000 cartas en el juego, y también no puede 
# entender como se formateaban los archivos .YDK.
# La segunda mejor opción me parece es pedirle al usuario que cargue un doc de Excel donde diga el nombre y
# utilidad de la carta y la cantidad

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

root =  Tk()
root.title("Deck Building Tool")
root.geometry("900x650")

# Para crear las pestañas lo puedo hacer con botones, estos botones una vez presionados cambian lo que se
# ve en pantalla
# pestnas será el espacio donde se pondrán los botones, Frame() me permite crear el espacio donde se pondrán
# los botones
pestanas = Frame(root)
pestanas.pack()


def show_tab(num_tab):
    '''
    Método que muestra la pestaña o botón seleccionado, este método se llama dentro de los botones que 
    corresponden a las pestañas, así se muestra el contenido de la pestaña que se quiere ver.
    
    Parametros:
        num_tab: corresponde al número de la pestaña que se quiere ver, en cada botón de cada pestaña se
                 le asigna el valor correspondiente a este parametro, tipo int
    '''
    tab_1_content.pack_forget()
    tab_2_content.pack_forget()
    tab_3_content.pack_forget()

    if num_tab == 1:
        tab_1_content.pack(fill = BOTH, expand = True)
    elif num_tab == 2:
        tab_2_content.pack(fill = BOTH, expand = True)
    elif num_tab == 3:
        tab_3_content.pack(fill = BOTH, expand = True)


# Creo los botones que funcionaran como pestañas
tab1_btn = Button(pestanas, text = "Crear mazo", bg = "gray", fg = "black", command = lambda: show_tab(1))
tab1_btn.pack(side = LEFT, padx = 10, pady = 5)

tab2_btn = Button(pestanas, text = "Calculadora Hipergeometrica", bg = "gray", fg = "black", 
                  command = lambda: show_tab(2))
tab2_btn.pack(side = LEFT, padx = 10, pady = 5)

tab3_btn = Button(pestanas, text = "Modo juego", bg = "gray", fg = "black", command = lambda: show_tab(3))
tab3_btn.pack(side = LEFT, padx = 10, pady = 5)

# Uso Frame() para crear el espacio donde voy a poner los botones y casillas de texto de cada pestaña
tab_1_content = Frame(root)
tab_2_content = Frame(root)
tab_3_content = Frame(root)

# Creo los botones y casillas de la pestaña 1, en este caso sería solamente una casilla donde se recibe
# la ruta del documento de Excel donde se tiene la lista del deck.
ruta_deck = Entry(tab_1_content, textvariable = StringVar(), font = ("Arial", 15))
ruta_deck.pack(padx = 10, pady = 10)

crear_deck_btn = Button(tab_1_content, text = "Crear mazo", bg = "gray", fg = "black", 
                  command = lambda: show_tab(2))
crear_deck_btn.pack(padx = 10, pady = 10)

# Inicializo las petañas en la primera, la de creación de deck pues lo primero que se espera es que el
# usuario creé el deck y luego haga las pruebas
show_tab(1)



# Ejecutar el bucle principal de Tkinter
root.mainloop()



# # adding menu bar in root window
# # new item in menu bar labelled as 'New'
# # adding more items in the menu bar 
# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)
 
# # adding a label to the root window
# lbl = Label(root, text = "Are you a Geek?")
# lbl.grid()
 
# # adding Entry Field
# txt = Entry(root, width=10)
# txt.grid(column =1, row =0)
 
 
# # function to display user text when
# # button is clicked
# def clicked():
 
#     res = "You wrote" + txt.get()
#     lbl.configure(text = res)
 
# # button widget with red color text inside
# btn = Button(root, text = "Click me" ,
#              fg = "red", command=clicked)
# # Set Button Grid
# btn.grid(column=2, row=0)
 
# # Execute Tkinter
# root.mainloop()
