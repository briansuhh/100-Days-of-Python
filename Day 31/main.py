from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import os
import sys

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- PATH ------------------------------- #
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ---------------------------- READ FILE ------------------------------- #
# If file not found or empty, read from original file
try:
    data = pd.read_csv(resource_path("./data/words_to_learn.csv"))
    to_learn = data.to_dict(orient="records")
except Exception:   
    data = pd.read_csv(resource_path("./data/french_words.csv"))
    to_learn = data.to_dict(orient="records")


# ---------------------------- CARD ------------------------------- #
def display_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    try:
        current_card = random.choice(to_learn)
    except IndexError:
        messagebox.showinfo(title="Congrats", message="You have learned all the words!") 
        return
    
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def remove_card():
    to_learn.remove(current_card)  
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    display_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) 

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=resource_path("./images/card_front.png"))
card_back = PhotoImage(file=resource_path("./images/card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


cross_img = PhotoImage(file=resource_path("./images/wrong.png"))
check_button = Button(image=cross_img, text="Check", highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR, cursor="hand2", command=display_card)
check_button.grid(row=1, column=0)

check_img = PhotoImage(file=resource_path("./images/right.png"))
cross_button = Button(image=check_img, text="Cross", highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR, cursor="hand2", command=remove_card)
cross_button.grid(row=1, column=1)

display_card()

window.mainloop()