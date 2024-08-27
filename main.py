
'''
_______________________________________________________________________________________________________________
if you want to use without installing the file:

fow windows:
            to run this code you will need customtkinter installed using "pip install customtkinter"
            or "uv pip install customtkinter" in your ide or code-editors terminal if you have uv pip installed

for mac:
        I looked online and suggest you do the same
_______________________________________________________________________________________________________________

just coppy the code in to your editor if you don't want to install the file as idk what else is in it,
I think I accidentally uploaded all my plugins in the git-file XD
_______________________________________________________________________________________________________________
'''

import customtkinter as ctk
import tkinter as tk
import string
import random

# Global variables
theme_text_colour = "#32CD32"  # Default green color
apptheme = "themes/green.json"

# Set initial theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme(apptheme)

# Initialize the window
root = ctk.CTk()
root.geometry("1500x950")
root.title("Not my password manager .exe")

'''
__________
functions
__________
'''

# Theme change functions
def theme_dark():
    global theme_text_colour, apptheme
    theme_text_colour = "#32CD32"  # Green text for dark theme
    apptheme = "themes/green.json"
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme(apptheme)
    update_widgets_theme()

def theme_light():
    global theme_text_colour, apptheme
    theme_text_colour = "#007bff"  # Blue text for light theme
    apptheme = "themes/blue.json"
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme(apptheme)
    update_widgets_theme()

# Function to update widgets' text color
def update_widgets_theme():
    label.configure(text_color=theme_text_colour)
    labele.configure(text_color=theme_text_colour)
    label2.configure(text_color=theme_text_colour)
    switch.configure(text_color=theme_text_colour)
    label_generate.configure(text_color=theme_text_colour)
    label_warning.configure(text_color=theme_text_colour)

    button_dark.configure(fg_color="gray30", hover_color="gray45", text_color="#000000")
    button_light.configure(fg_color="gray85", hover_color="gray70", text_color="#000000")
    button_encrypt.configure(fg_color=theme_text_colour, hover_color="lightgreen")

    button2_generate.configure(fg_color="gray30", hover_color="gray45", text_color="#000000")
    button2_generate.configure(fg_color="gray85", hover_color="gray70", text_color="#000000")
    button2_generate.configure(fg_color=theme_text_colour, hover_color="lightgreen")


# Process for encryption/decryption
def update_variable():
    global switch_state
    if switch.get() == 1:  # ON state
        switch_state = 1
        lable_state = "Password To Decrypt"
    else:  # OFF state
        switch_state = 2
        lable_state = "Password To Encrypt"
    labele.configure(text=lable_state)

def start_encryption():
    password = entry1.get()
    key = entry2.get()
    key = [char for char in key]
    password = password.replace(" ", "")

    cipher_text = ""
    if switch_state == 1:  # decryption
        chars = key
        decryption_tool = string.punctuation + string.digits + string.ascii_letters
        decryption_tool = list(decryption_tool)
        for letter in password:
            index = chars.index(letter)
            cipher_text += decryption_tool[index]
    elif switch_state == 2:  # encryption
        chars = string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        for letter in password:
            index = chars.index(letter)
            cipher_text += key[index]

    label1.insert(tk.END, cipher_text)
    label1.see(tk.END)

# Generate encryption key
def generate_key():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    random.shuffle(chars)
    new_chars = ''.join(chars)
    textbox.insert(tk.END, new_chars)
    textbox.see(tk.END)

'''
____________________
widgets top frame
____________________
'''

# Create UI components
frame = ctk.CTkFrame(
    master=root
)
frame.pack(
    pady=12,
    padx=12,
    fill="both",
    expand=True
)

label = ctk.CTkLabel(
    master=frame,
    text="Encrypt Or Decrypt",
    text_color=theme_text_colour,
    font=("consolas", 24)
)
label.pack(
    pady=12,
    padx=10
)

labele = ctk.CTkLabel(
    master=frame,
    text="Password To Encrypt",
    text_color=theme_text_colour,
    font=("consolas", 12)
)
labele.pack(
    pady=2,
    padx=2
)

entry1 = ctk.CTkEntry(
    master=frame,
    placeholder_text="Password to Encrypt:"
)
entry1.pack(
    pady=12,
    padx=10
)

switch = ctk.CTkSwitch(
    master=frame,
    text="En / De Crypt",
    text_color=theme_text_colour,
    command=update_variable
)
switch.pack(
    pady=12,
    padx=10
)

label2 = ctk.CTkLabel(
    master=frame,
    text="Encryption Key:",
    text_color=theme_text_colour,
    font=("consolas", 12)
)
label2.pack(
    pady=2,
    padx=2
)

entry2 = ctk.CTkEntry(
    master=frame,
    placeholder_text="encryption key:"
)
entry2.pack(
    pady=12,
    padx=10
)

button_encrypt = ctk.CTkButton(
    master=frame,
    text="En/De-Crypt",
    corner_radius=8,
    command=start_encryption,
    text_color="#000000"
)
button_encrypt.pack(
    pady=12,
    padx=10
)

label1 = ctk.CTkTextbox(
    master=frame
)
label1.pack(
    pady=2,
    padx=2
)

# Dark and Light theme buttons
button_dark = ctk.CTkButton(
    master=frame,
    text="Dark mode",
    font=("consolas",24),
    corner_radius=8,
    command=theme_dark,
    fg_color="#32CD32"
)
button_dark.place(
    x=10,
    y=10
)

button_light = ctk.CTkButton(master=frame, text="Light mode", font=("consolas", 24), corner_radius=8, command=theme_light)
button_light.place(
    x=10,
    y=50
)


'''
____________________
widgets bottom frame
____________________
'''

# Generate key section
frame2 = ctk.CTkFrame(
    master=root
)
frame2.pack(
    pady=12,
    padx=12,
    fill="both",
    expand=True
)

label_generate = ctk.CTkLabel(
    master=frame2,
    text="Generate a key",
    text_color=theme_text_colour,
    font=("consolas", 24)
)
label_generate.pack(
    pady=12,
    padx=10
)

button2_generate = ctk.CTkButton(
    master=frame2,
    text="Generate a key",
    corner_radius=8,
    command=generate_key,
    text_color="#000000",
    fg_color="#32CD32"
)
button2_generate.pack(
    pady=5,
    padx=10
)

textbox = ctk.CTkTextbox(
    master=frame2
)
textbox.pack(
    pady=0,
    padx=20
)

label_warning = ctk.CTkLabel(
    master=frame2,
    text="write down your key somewhere, if you lose it you lose everything. store it in a text file or something",
    text_color=theme_text_colour,
    font=("consolas", 10)
)
label_warning.pack(
    pady=12,
    padx=10
)

# Run the application
root.mainloop()

'''
____________________________________________________________________________________________________
this is my 1st time making a complex program with ui that isn't interacted with using the terminal
if its not the most efficient thing in the world as i learn it may be updated in the future
____________________________________________________________________________________________________
'''
