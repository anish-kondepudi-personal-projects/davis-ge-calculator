import requests
from bs4 import BeautifulSoup
from csv import writer

# Scrapes UC Davis's Site and creates .csv file with all Davis Majors along with URL to more information on that major
def scrape_majors():

	url = "https://ucdavis.pubs.curricunet.com/Catalog/degrees"

	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")

	majors = soup.find_all(class_="program-summary-wrapper")[1].find_all("p")

	majors_name_list = []
	majors_url_list = []
	for major in majors:
		try:
			majors_name_list.append((major.find('a').get_text()))
			majors_url_list.append((major.find('a')['href']))
		except AttributeError:
			None
			# AttributeError: 'NoneType' object has no attribute 'get_text'
			# * Master's degree offered only en route to Ph.D.

	with open("davis_majors.csv", "w") as file:
		csv_writer = writer(file)
		csv_writer.writerow(['Major Name', 'Major URL'])
		i = 0
		while i < min(len(majors_name_list),len(majors_url_list)):
			csv_writer.writerow([majors_name_list[i], majors_url_list[i]])
			i += 1

	pass

# scrape_majors()

