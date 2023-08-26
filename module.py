import logging
from colors import print_color

logger = logging.getLogger("MAIN")

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
         