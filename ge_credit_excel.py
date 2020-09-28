import xlrd
# Excel Sheet Data Downloaded from https://registrar-apps.ucdavis.edu/courses/ge_courses_byterm/index.cfm
# Must be Updated Every Quarter - Currently Updated as of 8/24/2020 for Fall Quarter 2020

# Returns Dictionary with all UC Davis Courses Paired with Units and satisfied GEs
def create_course_ge_dict():

	path = "davis_ge.xlsx"

	input_workbook = xlrd.open_workbook(path)
	input_worksheet = input_workbook.sheet_by_index(0)

	tot_rows = input_worksheet.nrows # Number of Rows
	tot_cols = input_worksheet.ncols # Number of Columns

	courses = []
	units = []
	topical_breadth = [] # AH, SE, SS
	core_literacies = [] # WE, OL, VL, ACGH, DD, WC, QL, SL - does not include English Composition, since that is specific to college

	for i in range(1, tot_rows):
		if input_worksheet.cell_value(i, 0) not in ('Prereq:', ''):
			courses.append(input_worksheet.cell_value(i, 0))
			if input_worksheet.cell_value(i, 1) != 'Var':
				units.append(input_worksheet.cell_value(i, 1))
			else:
				units.append(0.0)
			temp = []
			if input_worksheet.cell_value(i, 2) == "AH":
				temp.append("AH")
			if input_worksheet.cell_value(i, 3) == "SE":
				temp.append("SE")
			if input_worksheet.cell_value(i, 4) == "SS":
				temp.append("SS")
			topical_breadth.append(temp)
			tmp = []
			if input_worksheet.cell_value(i, 5) == "ACGH":
				tmp.append("ACGH")
			if input_worksheet.cell_value(i, 6) == "DD":
				tmp.append("DD")
			if input_worksheet.cell_value(i, 7) == "OL":
				tmp.append("OL")
			if input_worksheet.cell_value(i, 8) == "QL":
				tmp.append("QL")
			if input_worksheet.cell_value(i, 9) == "SL":
				tmp.append("SL")
			if input_worksheet.cell_value(i, 10) == "VL":
				tmp.append("VL")
			if input_worksheet.cell_value(i, 11) == "WC":
				tmp.append("WC")
			if input_worksheet.cell_value(i, 12) == "WE":
				tmp.append("WE")
			core_literacies.append(tmp)

	course_ge = {}
	j = 0
	while j < len(courses):
		course_ge.update({courses[j]: [units[j], topical_breadth[j], core_literacies[j]]})
		j += 1

	# print(course_ge['MAT 021C'])

	return course_ge

