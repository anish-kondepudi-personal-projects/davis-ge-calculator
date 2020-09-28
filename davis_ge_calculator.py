from major_name_to_url import get_courses
from ge_credit_excel import create_course_ge_dict

course_to_ge = create_course_ge_dict()
courses = get_courses()

course_info = {}
for course in courses:
	try:
		course_info.update({course: [course_to_ge[course][0], course_to_ge[course][1], course_to_ge[course][2]]})
	except KeyError:
		None

# Topical Breadth
AH = 0 # 12-20 Units
SE = 0 # 12-20 Units
SS = 0 # 12-20 Units

# Core Literacies
WE = 0 # 6 Units
OL = 0 # 3 Units
VL = 0 # 3 Units
ACGH = 0 # 3 Units
DD = 0 # 3 Units
WC = 0 # 3 Units
QL = 0 # 3 Units
SL = 0 # 3 Units

for course in course_info.keys():
	if 'AH' in course_info[course][1] or 'SE' in course_info[course][1] or 'SS' in course_info[course][1]:
		if 'AH' in course_info[course][1] and AH < 20:
			AH += course_info[course][0]
		elif 'SE' in course_info[course][1] and SE < 20:
			SE += course_info[course][0]
		elif 'SS' in course_info[course][1] and SE < 20:
			SS += course_info[course][0]

for course in course_info.keys():
	if 'WE' in course_info[course][2] or 'OL' in course_info[course][2] or 'VL' in course_info[course][2] or 'ACGH' in course_info[course][2] or 'DD' in course_info[course][2] or 'WC' in course_info[course][2] or 'QL' in course_info[course][2] or 'SL' in course_info[course][2]:
		if 'WE' in course_info[course][2] and WE < 6:
			WE += course_info[course][0]
		if 'OL' in course_info[course][2] and OL < 3:
			OL += course_info[course][0]
		if 'VL' in course_info[course][2] and VL < 3:
			VL += course_info[course][0]
		if 'ACGH' in course_info[course][2] and ACGH < 3:
			ACGH += course_info[course][0]
		if 'DD' in course_info[course][2] and DD < 3:
			DD += course_info[course][0]
		if 'WC' in course_info[course][2] and WC < 3:
			WC += course_info[course][0]
		if 'QL' in course_info[course][2] and QL < 3:
			QL += course_info[course][0]
		if 'SL' in course_info[course][2] and SL < 3:
			SL += course_info[course][0]

# print(f"AH: {AH}")
# print(f"SE: {SE}")
# print(f"SS: {SS}")

# print(f"WE: {WE}")
# print(f"OL: {OL}")
# print(f"VL: {VL}")
# print(f"ACGH: {ACGH}")
# print(f"DD: {DD}")
# print(f"WC: {WC}")
# print(f"QL: {QL}")
# print(f"SL: {SL}")

print("\n-----------------------------------------\n")
if AH + SE + SS >= 52:
	print("All Topical Breadth GEs have been satisfied.\n")
else:
	remaining = 52 - AH - SE - SS
	print("Topical Breadth GEs have NOT been satisfied.")
	if AH >= 20:
		print("You have satisfied all AH credits")
	else:
		print(f"> You have completed {int(AH)}/20 AH credits")
	if SE >= 20:
		print(f"> You have satisfied all SE credits")
	else:
		print(f"> You have completed {int(SE)}/20 SE credits")
	if SS >= 20:
		print("> You have satisfied all SS credits")
	else:
		print(f"> You have completed {int(SS)}/20 SS credits")
	print(f"You must complete {int(remaining)} more credits to satisfy Topical Breadth GEs.")
print("\n-----------------------------------------\n")
if WE >= 6 and OL >= 3 and VL >= 3 and ACGH >= 3 and DD >= 3 and WC >= 3 and QL >= 3 and SL >= 3:
	print("All Core Literacies GEs have been satisfied.")
else:
	print("Core Literacies GEs have NOT been satisfied.")
	if WE >= 6:
		print("> You have satisfied all WE credits")
	else:
		print(f"> You have completed {int(WE)}/6 WE credits")
	if OL >= 3:
		print("> You have satisfied all OL credits")
	else:
		print(f"> You have completed {int(OL)}/3 OL credits")
	if VL >= 3:
		print("> You have satisfied all VL credits")
	else:
		print(f"> You have completed {int(VL)}/3 VL credits")
	if ACGH >= 3:
		print("> You have satisfied all ACGH credits")
	else:
		print(f"> You have completed {int(ACGH)}/3 ACGH credits")
	if DD >= 3:
		print("> You have satisfied all DD credits")
	else:
		print(f"> You have completed {int(DD)}/3 DD credits")
	if WC >= 3:
		print("> You have satisfied all WC credits")
	else:
		print(f"> You have completed {int(WC)}/3 WC credits")
	if QL >= 3:
		print("> You have satisfied all QL credits")
	else:
		print(f"> You have completed {int(OL)}/3 OL credits")
	if SL >= 3:
		print("> You have satisfied all SL credits")
	else:
		print(f"> You have completed {int(SL)}/3 QL credits")
print("\n-----------------------------------------\n")
