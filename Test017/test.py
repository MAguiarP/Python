import tkinter as tk
from tkinter import filedialog

def save_file():
    text = text_widget.get("1.0", "end-1c")  # Get the text from the text widget
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)
        status_label.config(text="File saved successfully")

# Create the main window
root = tk.Tk()
root.title("Text Editor")

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack()

# Create a Save button
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

# Create a status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()