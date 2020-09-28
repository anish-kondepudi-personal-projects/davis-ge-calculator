from major_courses_csv_grabber import get_majors
from user_data_scrapper import get_user_data
from bs4 import BeautifulSoup
import requests

# Used within other function
def get_url(major_data, user_major):
	for major in major_data:
		if major[0][:4] == user_major[:4] and major[0][-4:] == user_major[-4:]:
			return major[1]
	return None

# Given a user's major, this function returns the URL to their major catalog
def major_to_catalog_url():
	major_data = get_majors("davis_majors.csv")
	user_major = get_user_data()
	url = get_url(major_data, user_major)
	return url

# Returns a list of an individuals courses depending on their major
def get_courses():
	catalog_url = major_to_catalog_url()
	response = requests.get(catalog_url)
	soup = BeautifulSoup(response.text, "html.parser")
	titles = soup.find_all(class_="course-entry-subject")
	nums = soup.find_all(class_="course-entry-course-number")
	t =[]
	n = []
	for title in titles:
		t.append(title.get_text())
	for num in nums:
		n.append(num.get_text())
	course = []
	i = 0
	while i < len(min(t,n)):
		course.append(t[i] + " " + n[i])
		i += 1
	course = list(dict.fromkeys(course)) # Removes Duplicates
	course_string = ''
	for c in course:
		course_string += c + ", "
	course_string = course_string[:-2] + "."
	print(f"\nWe found that you must finish the following courses in order to satisfy major requirements: \n-----------------------------------------------------------------------\n{course_string}\n-----------------------------------------------------------------------")
	ans = input("Is this information correct? (y/n) ")
	while True:
		while ans not in ('y','n'):
			print("Please type 'y' for yes or 'n' for no.")
			answer = input("Is this information correct? (y/n) ")
		if ans == 'y':
			return course
		else:
			res1 = input("\nWould you like to add or remove a course to the existing list? (y/n) ")
			while res1 not in ('y','n'):
				print("Please type 'y' for yes or 'n' for no.")
				res1 = input("\nWould you like to remove or add a course to the existing list? (y/n)")
			if res1 == "y":
				res2 = input("\nWhat would you like to do? (r/a)\nr - remove\na - add\n")
				while res2 not in ('r','a'):
					print("Please type 'r' remove or 'a' for add")
					res2 = input("Would you like to remove or add a course to the existing list? (r/a) ")
				if res2 == 'r':
					rem = input("What course would you like to remove? ")
					removed = course.pop(course.index(rem))
					print(f"{removed} has been removed.")
				else:
					ad = input("What course would you like to add? ")
					course.append(ad)
					print(f"{ad} had been added.")
			else:
				break
	return course	



# print(get_courses())