from tkinter import *
import customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.title('Text Editor')
root.geometry('1024x650')
root.resizable(False, False)

mode = "dark"


def change():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
        # Clear text box
        my_text.delete(0.0, END)
        my_text.insert(END, "What is in your mind...")
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"
        # Clear text box
        my_text.delete(0.0, END)
        my_text.insert(END, "What is in your mind...")

def open_file():
    file = filedialog.askopenfile(title="Open File", filetypes=[("Text Files", "*.txt")])
    if file:
        my_text.delete(0.0, END)
        my_text.insert(END, file.read())
        file.close()

def save_file():
    file = filedialog.asksaveasfile(title="Save File", filetypes=[("Text Files", "*.txt")], defaultextension=".txt")
    if file:
        file.write(my_text.get(0.0, END))
        file.close()

def open_folder():
    folder = filedialog.askdirectory(title="Open Folder")
    if folder:
        print(f"Folder opened: {folder}")



my_text = customtkinter.CTkTextbox(root, width=900, height=300)
my_text.pack(pady=20)

button_frame = customtkinter.CTkFrame(root)
button_frame.pack(pady=10)

open_button = customtkinter.CTkButton(button_frame, text="Open File", command=open_file)
open_button.pack(side=LEFT, padx=10)

save_button = customtkinter.CTkButton(button_frame, text="Save File", command=save_file)
save_button.pack(side=LEFT, padx=10)

folder_button = customtkinter.CTkButton(button_frame, text="Open Folder", command=open_folder)
folder_button.pack(side=LEFT, padx=10)

mode_button = customtkinter.CTkButton(root, text="Change Light/Dark", command=change)
mode_button.pack(pady=20)

about_frame = customtkinter.CTkFrame(root)
about_frame.pack(pady=20)

dev_info = customtkinter.CTkLabel(about_frame, text="Developed by ♡ Oussama Driouech",width=250)
dev_info.pack(pady=10)




root.mainloop()