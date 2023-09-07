import customtkinter as ctk

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(n_days):
	return(f"{n_days} days are {n_days * calculation_to_units} {name_of_unit} \n")

def validate_and_execute():	
	n_days_input = entry1.get()
	try:
		input_data = int(n_days_input)

		if input_data > 0:
			convertion = days_to_units(input_data)
			result.configure(text=convertion)
		elif input_data == 0:
			result.configure(text="you entered a 0, please enter a valid positive number")
			# result.configure(text="you entered a 0, please enter a valid positive number", fg="red")
		else:
			# result.configure(text="you entered a negative number, no conversion for you!", foreground="yellow", background="red")
			result.configure(text="you entered a negative number, no conversion for you!")
	except ValueError:
		result.configure(text="your input is not a valid number\nDon't ruin my program!")

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('500x500')

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Days to hours converter', font=('Arial', 20))
label.pack(pady=12)

entry1 = ctk.CTkEntry(master=frame, placeholder_text='Days to convert')
entry1.pack(pady=12, padx=10)

button1 = ctk.CTkButton(master=frame, text='calculate', command=validate_and_execute)
button1.pack(pady=12, padx=10)

result = ctk.CTkLabel(master=frame, text='Total hours =', font=('Arial', 20), wraplength=300)
result.pack(pady=12)


root.mainloop() 
