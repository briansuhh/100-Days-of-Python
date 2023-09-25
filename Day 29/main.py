from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import os
import sys

FONT = ("Arial", 11, "normal")

# ---------------------------- PATH ------------------------------- #
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.config(fg='black')
    password_entry.delete(0, END)

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
               "j", "k","l", "m", "n", "o", "p", "q", "r",
               "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = [*letters_list, *numbers_list, *symbols_list]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        if messagebox.askokcancel(title=website, message=f"Email: {email} \nPassword: {password} \n\nPress OK to save."):

            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- PLACEHOLDERS ------------------------------- #
def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg='black')  # Change text color if needed

def on_entry_leave(event, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg='gray')  # Reset text color if needed


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=10)
window.geometry("+600+300")
icon = resource_path("logo.ico")
window.iconbitmap(icon)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file=resource_path("logo.png"))
canvas.create_image(100, 100, image=lock_img)
canvas.pack()

website_entry = Entry(window, fg='gray', font=FONT)
website_entry.insert(0, "Enter Website")
website_entry.bind("<FocusIn>", lambda event, entry=website_entry, placeholder="Enter Website": on_entry_click(event, entry, placeholder))
website_entry.bind("<FocusOut>", lambda event, entry=website_entry, placeholder="Enter Website": on_entry_leave(event, entry, placeholder))
website_entry.focus()
website_entry.pack()

email_entry = Entry(window, fg='gray', font=FONT)
email_entry.insert(0, "Enter Email")
email_entry.bind("<FocusIn>", lambda event, entry=email_entry, placeholder="Enter Email": on_entry_click(event, entry, placeholder))
email_entry.bind("<FocusOut>", lambda event, entry=email_entry, placeholder="Enter Email": on_entry_leave(event, entry, placeholder))
email_entry.pack()

password_entry = Entry(window, fg='gray', font=FONT)  # Use show="*" to hide the password
password_entry.insert(0, "Enter Password")
password_entry.bind("<FocusIn>", lambda event, entry=password_entry, placeholder="Enter Password": on_entry_click(event, entry, placeholder))
password_entry.bind("<FocusOut>", lambda event, entry=password_entry, placeholder="Enter Password": on_entry_leave(event, entry, placeholder))
password_entry.pack()

#buttons
generate_password_button = Button(text="Generate Password", width=15, font=FONT, command=generate_password, cursor='hand2')
generate_password_button.pack(side='left', padx=5, pady=5)

submit_button = Button(text="Submit", width=10, font=FONT, command=save_password, cursor='hand2')
submit_button.pack(side='right', padx=5, pady=5)


window.mainloop()
