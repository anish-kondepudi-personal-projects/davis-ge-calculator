import requests
from bs4 import BeautifulSoup

# Given a user's first and last name, this function returns the user's major
# Add a try/except block to fix issue of not finding a user
def get_user_data():
	first_name = input("What is your first name? ").lower()
	last_name = input("What is your last name? ").lower()

	# first_name = 'anish'
	# last_name = 'kondepudi'

	url = f"https://directory.ucdavis.edu/search/directory_results.shtml?filter={first_name}%20{last_name}"

	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")

	data = soup.find(class_="panel-pane box").find_all('tr')

	print("User Data:\n---------------")

	for piece in data:
		p = piece.get_text()
		if p[:4] == 'Name':
			print(f"Name: {p[4:]}")
		elif p[:6] == 'E-mail':
			temp = p.split(" ")
			print(f"Email: {temp[1]}")
		elif p[:13] == 'Student Level':
			print(f"Grade: {p[14:]}")
		elif p[:5] == 'Major':
			print(f"Major: {p[6:]}")
			major = p[6:]
		# else:
			# print(p)
	# print(data)
	print("---------------")
	answer = input("Is this information correct? (y/n) ")
	while answer not in ('y','n'):
		print("Please type 'y' for yes or 'n' for no.")
		answer = input("Is this information correct? (y/n) ")
	if answer == 'n':
		major = input("What is your major at UC Davis? ")
	print("Please wait while we scrape UC Davis's site for the courses required for your major.")
	return major

# print(get_user_data())