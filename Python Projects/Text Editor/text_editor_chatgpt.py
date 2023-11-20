# First, we need to tell the computer to use a special tool called tkinter.
import tkinter as tk
# Then, we ask tkinter to get a tool called filedialog from its box.
from tkinter import filedialog

# Next, we create a function called open_file.


def open_file():
    # Inside this function, we ask the computer to find and show us a file.
    file_path = filedialog.askopenfilename()
    # If the computer finds a file and we choose one, it reads what's inside the file.
    if file_path:
        # Then, it shows the words from the file on our editor.
        with open(file_path, 'r') as file:
            editor.delete('1.0', tk.END)
            editor.insert(tk.END, file.read())

# After that, we create another function called save_file.


def save_file():
    # This function helps us to save our writing into a file.
    # It asks where we want to save it and what name we want to give.
    file_path = filedialog.asksaveasfilename(
        defaultextension='.txt', filetypes=[("Text files", "*.txt")])
    # If we choose a place to save and give a name, the computer writes what we wrote in the editor into the file.
    if file_path:
        with open(file_path, 'w') as file:
            file.write(editor.get('1.0', tk.END))


# Now, we create a special window where we can write and see our writing.
root = tk.Tk()
# We give it a name at the top of the window.
root.title("Simple Text Editor")

# Here, we make a menu bar at the top of our window.
menu = tk.Menu(root)
root.config(menu=menu)

# Inside the menu bar, we make a part called "File" where we put some options.
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
# We add choices like "Open" and "Save" to this part of the menu.
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
# There's also an option to "Exit" or close our program.
file_menu.add_command(label="Exit", command=root.quit)

# This is where we can write and see our words. It's like our notepad.
editor = tk.Text(root, wrap="word")
# We put the notepad in our window and stretch it so we can write a lot.
editor.pack(expand=True, fill="both")

# Finally, we ask the computer to show everything we made in the window.
root.mainloop()
