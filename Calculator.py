from tkinter import *
import tkinter as tk
from typing import List,Union,Any

# je définis la fonct. qui permet d'appuy. sur une touche

expression = ""


root = tk.Tk ()


def press ( touch ):
    if touch == "=":
        calculate ()
        return

    global expression
    expression += str ( touch )
    equation.set ( expression )


def calculate ():
    try:
        global expression
        total = str (eval ( expression))

        equation.set ( total)
        expression = total
    except:
        equation.set("erreur")
        expression = ""


def delete ():
    global expression
    expression = ""
    equation.set ("")

if __name__ == "main":
    root = Tk()

    root.geometry ( '880x880')
    root.title ( " || Calculatrice 9000 Version 1.0 || " )
    root.resizable ( 0,0 )
    root.configure ( background = "red" )
    equation = StringVar ()  # variable qui sert à stocker le contenu actuel

    # Boîte de résultat
    result_box = Label(root, bg = "black",fg = "white",textvariable = equation, height = "3")
    result_box.grid(columnspan=4)

# Création des boutons avec des lambda fonctions
'''button_0 = tk.Button ( root,text = "0",command = lambda: button_click ( 0 ) )
button_1 = tk.Button ( root,text = "1",x )
button_2 = tk.Button ( root,text = "2",command = lambda: button_click ( 2 ) )
button_3 = tk.Button ( root,text = "3",command = lambda: button_click ( 3 ) )
button_4 = tk.Button ( root,text = "4",command = lambda: button_click ( 4 ) )
button_5 = tk.Button ( root,text = "5",command = lambda: button_click ( 5 ) )
button_6 = tk.Button ( root,text = "6",command = lambda: button_click ( 6 ) )
button_7 = tk.Button ( root,text = "7",command = lambda: button_click ( 7 ) )
button_8 = tk.Button ( root,text = "8",command = lambda: button_click ( 8 ) )
button_9 = tk.Button ( root,text = "9",command = lambda: button_click ( 9 ) )
button_operator = tk.Button ( root,text = "/",command = lambda: button_click ( 10 ) )
button_operator = tk.Button ( root,text = "*",command = lambda: button_click ( 11 ) )'''

button_labels: list[Union[str, Any]] = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","+","="
]
# self.createButton('sin', 4, 0, commande=partial(self.modifier_calcul, 'sin(', 'sin('), bgcolor='purple')
buttons = [1,2,3,4,5,6,7,8,9,"sin","cos"]

row = 2
column = 2

for button in buttons:
    b = Label ( root,text = str ( button ),bg = 'orange',fg = "white",height = 4,width = 6 )
    b.bind ( "<Button-1>",lambda e,button=button: press ( button ) )

    b.grid ( row = row, column = column )

    column += 1
    if column == 3:
        column = 0
        row += 1

b = Label ( root,text = "Effacer",bg = 'black',fg = "white",height = 5,width = 7 )
b.bind ( "<Button-1>",lambda e: delete () )
b.grid ( columnspan = 5 )



root.mainloop ()
