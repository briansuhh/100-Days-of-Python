import tkinter

def calculate():
    result = float(input.get()) * 1.60934
    result_label.config(text=result)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)
window.geometry("+550+350")


# Entry
input = tkinter.Entry()
input.grid(row=1, column=2)
input.config(width=15, justify="center", font=("Arial", 12), borderwidth=2)
input.focus()

# Label
miles = tkinter.Label(text="miles", font=("Arial", 13))
miles.grid(row=1, column=3)

# Label
km = tkinter.Label(text="km", font=("Arial", 13))
km.grid(row=2, column=3)

# Label
equal_to = tkinter.Label(text="is equal to", font=("Arial", 13))
equal_to.grid(row=2, column=1)

# Label
result_label = tkinter.Label(text="0", font=("Arial", 13, "bold"))
result_label.grid(row=2, column=2)
result_label.config(padx=10, pady=10)

# Button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=3, column=2) 
button.config(width=10, borderwidth=2, font=("Arial", 10, "bold"))
button.focus()


window.mainloop()