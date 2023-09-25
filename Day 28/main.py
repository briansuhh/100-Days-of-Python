from tkinter import *
import os
import sys


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None    


# ---------------------------- PATH ------------------------------- #
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:     
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:   
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:               
        count_down(work_sec)
        title_label.config(text="Study", fg=GREEN)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps < 8:
            start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry("+465+250")

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", bg=GREEN, fg=BLACK, font=(FONT_NAME, 10), command=start_timer)  
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", bg=RED, fg=BLACK, font=(FONT_NAME, 10), command=reset_timer)  
reset_button.grid(row=3, column=3)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_marks.grid(row=4, column=2)


window.mainloop()

