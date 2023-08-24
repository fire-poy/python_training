from module import validate_and_execute
# import module ---> imports all module
# apres il faut la sintaxe est: module.validate_and_execute()
# from module import * ---> imports all module
# import module as md ---> imports all module and rename it

user_input = ""
while user_input != "exit":
	print("---------------------------------------------------------------------------------")

	user_input_prompt = "Enter number of days and conversion unit ---> "
	user_input = input(user_input_prompt)
	days_and_unit = user_input.split(":")
	days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
	validate_and_execute(days_and_unit_dict)
