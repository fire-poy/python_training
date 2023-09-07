import requests
from colors import print_color

# select API (github, gitlab)

# select user
# if not found print error message
response = requests.get("https://api.github.com/users/fire-poy/repos")
my_projects = response.json()
# print(my_projects[0])
for project in my_projects:
	print_color(f"Project name= {project['name']}", "red")
	# print_color(f"description: {project['description']}", "green")
    # print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")

total_projects = len(my_projects)
print_color(f"Total number of projects: {total_projects}", "yellow")
