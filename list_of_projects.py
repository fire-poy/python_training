import requests
from colors import print_color

# select API (github, gitlab)

# select user
# if not found print error message
response = requests.get("https://api.github.com/users/NeuralNine/repos")
my_projects = response.json()
# print(my_projects[0])
for project in my_projects:
	print_color(f"Project name: {project['name']}", "red")
	print_color(f"Description:  {project['description']}", "red")
	print_color(f"Project Url:  {project['html_url']}", "red")
	print()
	# print_color(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n", "blue")
	# for key, value in project.items():
		# print(key, value)
		# print(key)
	# print()


        

total_projects = len(my_projects)
print_color(f"Total number of projects: {total_projects}", "yellow")