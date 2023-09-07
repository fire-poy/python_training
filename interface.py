import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('500x500')

def login():
    print('Login')
    
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login', font=('Arial', 20))
label.pack(pady=12)

entry1 = ctk.CTkEntry(master=frame, placeholder_text='Username')
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text='Password', show='*')
entry2.pack(pady=12, padx=10)

button1 = ctk.CTkButton(master=frame, text='Login', command=login)
button1.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember me')
checkbox.pack(pady=12, padx=10)

root.mainloop() 
