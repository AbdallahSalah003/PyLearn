import tkinter as tk
from tkinter import filedialog, colorchooser, font, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                text_editor.delete(1.0, tk.END)
                text_editor.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_editor.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def cut_text():
    text_editor.event_generate("<<Cut>>")

def copy_text():
    text_editor.event_generate("<<Copy>>")

def paste_text():
    text_editor.event_generate("<<Paste>>")

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_editor.config(fg=color)

def change_font(font_name, font_size):
    current_font = font.Font(font=text_editor["font"])
    current_font.config(family=font_name, size=font_size)
    text_editor.config(font=current_font)

def update_status(event=None):
    row, col = text_editor.index(tk.INSERT).split('.')
    status_bar.config(text=f"Line: {row} | Column: {col}")

def exit_editor():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Advanced Text Editor")
root.geometry("800x600")

# Create a Text widget
text_editor = tk.Text(root, wrap='word', undo=True)
text_editor.pack(fill=tk.BOTH, expand=1)
text_editor.bind("<KeyRelease>", update_status)

# Create a Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Add Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Add Format menu
format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Text Color", command=choose_color)

# Add Font submenu
font_menu = tk.Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font", menu=font_menu)

# Add font options
font_names = ["Arial", "Courier", "Helvetica", "Times"]
font_sizes = [10, 12, 14, 16, 18, 20, 24]

for font_name in font_names:
    font_menu.add_command(label=font_name, command=lambda name=font_name: change_font(name, int(text_editor['font'].split(' ')[1])))

font_size_menu = tk.Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font Size", menu=font_size_menu)

for size in font_sizes:
    font_size_menu.add_command(label=str(size), command=lambda size=size: change_font(text_editor['font'].split(' ')[0], size))

# Add Status bar
status_bar = tk.Label(root, text="Line: 1 | Column: 1", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Run the application
root.mainloop()
