from csv import reader

# Given a .csv file with UC Davis's Majors and URLs to information about those majors, this function
# returns a list containing that information
def get_majors(filename):
	davis_majors = []
	with open(filename, "r") as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if row != []:
				davis_majors.append(row)
	davis_majors.pop(0)
	return davis_majors

# print(get_majors("davis_majors.csv"))
