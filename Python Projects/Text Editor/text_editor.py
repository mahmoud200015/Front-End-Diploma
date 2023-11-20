"""
1. Make a design
2. Understand the python GUI lib
3. Save as - open file - textbox to enter text
"""

import tkinter as tk
from tkinter.filedialog import *

def open_file():
  file_path = askopenfilename(
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
  )
  if not file_path:
    return
  txt_edit.delete(1.0, "end") # tk.END= "end"

  with open(file_path, "r") as input_file:
    text = input_file.read()
    txt_edit.insert(tk.END, text)
  window.title(f"Almdrasa Text Editor - {file_path}")

def save_file():
  file_path = asksaveasfilename(
      defaultextension="txt",
      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
  )

  if not file_path:
    return
  
  with open(file_path, "w") as output_file:
    text = txt_edit.get(1.0, tk.END)
    output_file.write(text)
  output_file.close()

  window.title(f"Almdrasa Text Editor - {file_path}")

window = tk.Tk()
window.title("Almdrasa Text Editor")
# window.geometry("600x600")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=600)

txt_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save As", command=save_file)

btn_open.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
btn_save.grid(column=0, row=1, sticky="ew", padx=5)

frame_buttons.grid(column=0, row=0, sticky="nw")
txt_edit.grid(column=1, row=0, sticky="nsew")


window.mainloop()
