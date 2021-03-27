#-*- coding: utf-8 -*-

import keyboard
import random
import time
from tkinter import * 

def logiciel():
        
    letter = ['Z', 'Q', 'S', 'D', 'C', 'space']
    def selectRandom(letter):
        return random.choice(letter)

    time.sleep(10.0)
    while True:
        time.sleep(1.0)
        keyboard.press_and_release(selectRandom(letter))
    
root = Tk()
root.title("AFK Bot By Jeceey")
root.geometry("720x480")
root.iconbitmap("logo.ico")
root.config(background='#34495e')

instructions = Label(root, text="Lorsque vous lancez le script, vous avez un delay de 10 secondes avant qu'il ne se mette en exécution", font="Raleway", bg='#34495e', fg='white')
instructions.pack()
instructions2 = Label(root, text="Pour fermer le logiciel maintenez ALT + F4", font="Raleway", bg='#34495e', fg='white')
instructions2.pack()

label = Label(root, text="AFK Bot", font=("Raleway", 30), bg='#34495e', fg='white')
label.pack()
label1 = Label(root, text="By Jeceey", font=("Raleway", 15), bg='#34495e', fg='white')
label1.pack()

launch = Button(root, text="Lancer", command=logiciel, fg='black')
launch.pack() 


root.mainloop()