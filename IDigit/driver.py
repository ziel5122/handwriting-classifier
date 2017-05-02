from Tkinter import *
import tkFont
from IDigit import IDigit
import pygame

num_neighbors = 9

root = Tk() #create TK window
root.title("i d i g i t         [Number Identifier]")
id_window = IDigit(root, num_neighbors)

button_font = tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD)
id_window.addButton("DRAWPAD", button_font, "black", "lightBlue", "white", "#00BFFF", id_window.drawpad, 12, LEFT) #add buttons
id_window.addButton("UPLOAD", button_font, "black", "LightGreen", "white", "#00BA37", id_window.setImage, 12, LEFT)
id_window.addButton("EXIT", button_font, "black", "pink", "white", "#FF0DF2", quit, 12, LEFT)

root.mainloop() #start program
