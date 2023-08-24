calculation_to_units = 24
name_of_unit = "hours"

def print_color(text, color):
	supported_colors = ("red", "green", "yellow", "blue")

	if (color not in supported_colors):
		print("Color is not supported")
	else:
		color_mapping = {
			"red": "\033[91m",
			"green": "\033[92m",
			"yellow": "\033[93m",
			"blue": "\033[94m"
		}
		reset = "\033[0m"

		print(color_mapping[color] + text + reset)

def days_to_units(n_days):
	return(f"{n_days} days are {n_days * calculation_to_units} {name_of_unit} \n")


def validate_and_execute():
	try:
		input_data = int(n_days_input)

		if input_data > 0:
			result = days_to_units(input_data)
			print_color(result, "green")
		elif input_data == 0:
			print_color("you entered a 0, please enter a valid positive number\n", "yellow")
		else:
			print_color("you entered a negative number, no conversion for you!\n", "yellow")
	except ValueError:
		print_color("your input is not a valid number. Don't ruin my program!\n", "red")
        
user_input = ""
while user_input != "exit":
	print("---------------------------------------------------------------------------------")
	user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hours!\nInsert days: ")
	list_of_days = user_input.split(", ")
	for n_days_input in set(list_of_days):
		validate_and_execute()

