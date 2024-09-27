import itertools
import string
import os
import sys
from tkinter import Tk, Label, Button, Entry, Text, StringVar

def generate_wordlist(name, num, upper, lower, symbols):
    characters = ''
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if symbols:
        characters += string.punctuation

    if not characters:
        return []

    wordlist = []
    for length in range(1, num + 1):
        for item in itertools.product(characters, repeat=length):
            wordlist.append(''.join(item))

    with open(name, 'w') as file:
        for word in wordlist:
            file.write(f"{word}\n")
    return wordlist

def cli_mode():
    if len(sys.argv) < 6:
        print("Usage: python wordlist_generator.py <filename> <max_length> <upper> <lower> <symbols>")
        return

    filename = sys.argv[1]
    max_length = int(sys.argv[2])
    upper = bool(int(sys.argv[3]))
    lower = bool(int(sys.argv[4]))
    symbols = bool(int(sys.argv[5]))

    generate_wordlist(filename, max_length, upper, lower, symbols)
    print(f"Wordlist generated: {filename}")

def gui_mode():
    def on_generate():
        name = filename_entry.get()
        num = int(max_length_entry.get())
        upper = upper_var.get()
        lower = lower_var.get()
        symbols = symbols_var.get()

        generate_wordlist(name, num, upper, lower, symbols)
        result_text.delete(1.0, 'end')
        result_text.insert('end', f"Wordlist generated: {name}\n")

    root = Tk()
    root.title("Wordlist Generator")

    Label(root, text="Filename:").pack()
    filename_entry = Entry(root)
    filename_entry.pack()

    Label(root, text="Max Length:").pack()
    max_length_entry = Entry(root)
    max_length_entry.pack()

    upper_var = StringVar(value="0")
    lower_var = StringVar(value="0")
    symbols_var = StringVar(value="0")

    Label(root, text="Include Uppercase (1/0):").pack()
    Entry(root, textvariable=upper_var).pack()

    Label(root, text="Include Lowercase (1/0):").pack()
    Entry(root, textvariable=lower_var).pack()

    Label(root, text="Include Symbols (1/0):").pack()
    Entry(root, textvariable=symbols_var).pack()

    Button(root, text="Generate", command=on_generate).pack()
    result_text = Text(root, height=10, width=50)
    result_text.pack()

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_mode()
    else:
        gui_mode()
