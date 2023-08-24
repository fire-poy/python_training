import logging

logger = logging.getLogger("MAIN")

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

def days_to_units(n_days, conversion_unit):
	if conversion_unit == "h":
		return(f"{n_days} days are {n_days * 24} hours\n")
	elif conversion_unit == "m":
		return(f"{n_days} days are {n_days * 24 * 60} minutes\n")
	elif conversion_unit == "s":
		return(f"{n_days} days are {n_days * 24 * 60 * 60} seconds\n")
	else:
		usage()
		return("unsupported unit")
	
def usage():
	print_color("usage ---> number_of_days:convertion_unit", "yellow")
	print_color("number of days must be a positive number", "yellow")
	print_color("convertion units: h, m, s", "yellow")
	print_color("example 2:h will print:", "yellow")
	days_to_units(2,"h")

def validate_and_execute(days_and_unit_dict):
	try:
		input_days = int(days_and_unit_dict["days"])

		if input_days > 0:
			result = days_to_units(input_days, days_and_unit_dict["unit"])
			print_color(result, "green")
		else:
			usage()
	except ValueError:
		logger.error("ValueError: You entered an invalid number. Don't ruin my program!")	
         