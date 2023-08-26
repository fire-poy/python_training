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
