BACKGROUND_COLOR = "#B1DDC6"

from operator import index
from re import L
from tkinter import *
import pandas
import random

window = Tk()
window.title("Flash Cash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

list_dict_word = []
RANDOM_WORD = []

try: 
    remain_word = pandas.read_csv("flash-card-project-start/data/word_to_learn.csv")
except FileNotFoundError:
    read_word = pandas.read_csv("flash-card-project-start/data/word_1001_to_1100_trandstion.csv")
    list_dict_word = read_word.to_dict(orient="records")
else:
    list_dict_word = remain_word.to_dict(orient="records")

#---------------------------------------- Button to chance word -----------------------------------------------------------------#

def press_button():
    global RANDOM_WORD
    global FLIP_CARD
    window.after_cancel(FLIP_CARD)
    RANDOM_WORD = random.choice(list_dict_word)
    canvas.itemconfig(text_word, text=RANDOM_WORD["English"], fill="black")
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(background, image=englist_png)
    FLIP_CARD = window.after(3000, next_card_3s)

def next_card_3s():
    canvas.itemconfig(text_word, text=RANDOM_WORD["Thai"], fill="white", font=("Ariel", 70))
    canvas.itemconfig(title_text, text="Thai", fill="white", font=("Ariel", 50, "italic"))
    canvas.itemconfig(background, image=thai_png)

def next_word():
    list_dict_word.remove(RANDOM_WORD)
    word_remain_to_learn = pandas.DataFrame(list_dict_word)
    word_remain_to_learn.to_csv("flash-card-project-start/data/word_to_learn.csv", index=False)
    press_button()

#---------------------------------------- UI -----------------------------------------------------------------#

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
englist_png = PhotoImage(file="flash-card-project-start/images/card_front.png")
thai_png = PhotoImage(file="flash-card-project-start/images/card_back.png")
button_yes_png = PhotoImage(file="flash-card-project-start/images/right.png")
button_no_png = PhotoImage(file="flash-card-project-start/images/wrong.png")

# ฺCard_front
background = canvas.create_image(400, 263, image=englist_png)
canvas.grid(column=0, row=0, columnspan=5)
title_text = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60))

FLIP_CARD = window.after(3000, next_card_3s)
# yes
button_yes = Button(image=button_yes_png, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
button_yes.grid(column=3, row=1)

# no
button_no = Button(image=button_no_png, highlightthickness=0, bg=BACKGROUND_COLOR, command=press_button)
button_no.grid(column=1, row=1)

press_button()




window.mainloop()