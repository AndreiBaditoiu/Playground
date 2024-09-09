import tkinter as tk

import pyjokes


def show_joke():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)


root = tk.Tk()
root.title('Jokes')
root.geometry('500x400')

joke_button = tk.Button(root, text='Joke', command=show_joke)
joke_button.pack(pady=20)

joke_label = tk.Label(root, text="", wraplength=500, justify='center')
joke_label.pack(pady=20)

root.mainloop()
