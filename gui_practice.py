import tkinter as tk

def submit():
    typed_answer = entry.get()
    print(f"You typed: {typed_answer}")

window = tk.Tk()

label = tk.Label(window, text="What is 2 + 2?")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()