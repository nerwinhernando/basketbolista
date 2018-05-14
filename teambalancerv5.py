import math
import csv
import os

print()
print()

# get number of teams for balancing
print("Getting Team Numbers for Balancing")
text_file = open('input parameters/team_number.txt', 'r')
team_number = text_file.readline().replace('\n', '')
print("Teams for balancing is " + team_number)
text_file.close()

print()

# locate source file path
print("Getting Filepath")
text_file = open('input parameters/file_path.txt', 'r')
file_path = text_file.readline().replace('\n', '')
print("File path is " + file_path)
text_file.close()

print()

# get destination file path
print("Getting Target Destination of Results")
text_file = open('input parameters/target_path.txt', 'r')
target_path = text_file.readline().replace('\n', '')
print("Target path is " + target_path)
text_file.close()

print()

# open file from filepath

Title = []
Name = []
Age = []
HomeAddress = []
ContactNos = []
Weight = []
Height = []
Position = []
PlayingYears = []
Achievement = []
ThankYouPage = []
ThankYouAll = []
ID = []
CreatedDate = []
UpdatedDate = []
Owner = []

print("Getting Raw Data form CSV File")
index = 0
import csv
with open(file_path, 'r') as csv_file:
	csv_file = csv.reader(csv_file)

	next(csv_file)

	for line in csv_file:
		Title.append(str(line[0]))
		Name.append(str(line[1]))
		Age.append(int(line[2]))
		HomeAddress.append(str(line[3]))
		ContactNos.append(str(line[4]))
		Weight.append(int(line[5]))
		Height.append(int(line[6]))
		Position.append(str(line[7]))
		PlayingYears.append(str(line[8]))
		Achievement.append(str(line[9]))
		ThankYouPage.append(str(line[10]))
		ThankYouAll.append(str(line[11]))
		ID.append(str(line[12]))
		CreatedDate.append(str(line[13]))
		UpdatedDate.append(str(line[14]))
		Owner.append(str(line[15]))
		index = index + 1

print("total Records: ", index)
no_players = index

Criterion_Height = []
Criterion_Weight = []
Criterion_PlayingYears = []
Criterion_Achievement = []
Criterion_Total = []

# height score computation
i = 0
for i in range(index):
	if Height[i] <= 148:
		Criterion_Height.append(30)
	elif 149 <= Height[i] <= 157:
		Criterion_Height.append(40)
	elif 158 <= Height[i] <= 166:
		Criterion_Height.append(50)
	elif 167 <= Height[i] <= 175:
		Criterion_Height.append(60)
	elif 176 <= Height[i] <= 185:
		Criterion_Height.append(70)
	elif 186 <= Height[i] <= 194:
		Criterion_Height.append(80)
	elif 195 <= Height[i] <= 202:
		Criterion_Height.append(90)
	elif Height[i] >= 203:
		Criterion_Height.append(100)
# print(i, Name[i], Criterion_Height[i])


# weight score computation using BMI and equivalences
i = 0
for i in range(index):
	if (Weight[i]/((Height[i]/100)*(Height[i]/100))) <= 18:  # bmi - extremely underweight
		Criterion_Weight.append(40)
	elif (19 <= (Weight[i]/((Height[i]/100)*(Height[i]/100)))) and (Weight[i]/((Height[i]/100)*(Height[i]/100)) <= 24):  # bmi - underweight
		Criterion_Weight.append(60)
	elif (25 <= (Weight[i]/((Height[i]/100)*(Height[i]/100)))) and (Weight[i]/((Height[i]/100)*(Height[i]/100)) <= 29):  # bmi - healthy
		Criterion_Weight.append(100)
	elif (30 <= (Weight[i]/((Height[i]/100)*(Height[i]/100)))) and (Weight[i]/((Height[i]/100)*(Height[i]/100)) <= 34):  # bmi - overweight
		Criterion_Weight.append(80)
	elif (35 <= (Weight[i]/((Height[i]/100)*(Height[i]/100)))) and (Weight[i]/((Height[i]/100)*(Height[i]/100)) <= 39):  # bmi - obese
		Criterion_Weight.append(60)
	elif (Weight[i]/((Height[i]/100)*(Height[i]/100))) >= 40:  # bmi - extremely obese
		Criterion_Weight.append(40)
# print(i, Name[i], Criterion_Weight[i])

# years playing score computation
i = 0
for i in range(index):
	# print(PlayingYears[i].upper())
	if PlayingYears[i].upper() == str("1-2 years").upper():
		Criterion_PlayingYears.append(40)
	elif PlayingYears[i].upper() == str("3-5years").upper():
		Criterion_PlayingYears.append(60)
	elif PlayingYears[i].upper() == str("6-10 years").upper():
		Criterion_PlayingYears.append(80)
	elif PlayingYears[i].upper() == str("11 years above").upper():
		Criterion_PlayingYears.append(100)
# print(i, Name[i], PlayingYears[i].upper(), Criterion_PlayingYears[i])

# past achievements score computation
i = 0
for i in range(index):
	# print(PlayingYears[i].upper())
	if Achievement[i].upper() == str("None").upper():
		Criterion_Achievement.append(40)
	elif Achievement[i].upper() == str("Individual Awardee (ROY, Most Improved, etc.)").upper():
		Criterion_Achievement.append(60)
	elif Achievement[i].upper() == str("Mythical 5 member").upper():
		Criterion_Achievement.append(80)
	elif Achievement[i].upper() == str("MVP").upper():
		Criterion_Achievement.append(100)
# print(i, Name[i], Achievement[i].upper(), Criterion_Achievement[i])

# total score computation
i = 0
for i in range(index):
	Criterion_Total.append((0.30 * Criterion_Height[i]) + (0.20 * Criterion_Weight[i]) + (0.20 * Criterion_PlayingYears[i]) + (0.30 * Criterion_Achievement[i]))
# print(i, ID[i], Name[i], Position[i], Criterion_Total[i])

Position_Center = []
Position_Forward = []
Position_Guard = []

# group by position
i = 0
for i in range(index):
	if Position[i].upper() == str("Guard").upper():
		Position_Guard.append([ID[i], Name[i].upper(), Position[i].upper(), Criterion_Total[i]])
	elif Position[i].upper() == str("Forward").upper():
		Position_Forward.append([ID[i], Name[i].upper(), Position[i].upper(), Criterion_Total[i]])
	elif Position[i].upper() == str("Center").upper():
		Position_Center.append([ID[i], Name[i].upper(), Position[i].upper(), Criterion_Total[i]])
# print(ID[i], Name[i], Position[i], Criterion_Total[i])

# rank descending by position
Ranked_Center = []
Ranked_Forward = []
Ranked_Guard = []
Ranked_Masterlist = []

Ranked_Guard = sorted(Position_Guard, key=lambda x: x[3], reverse=False)
Ranked_Forward = sorted(Position_Forward, key=lambda x: x[3], reverse=False)
Ranked_Center = sorted(Position_Center, key=lambda x: x[3], reverse=False)

# print("Guard", len(Ranked_Guard), Ranked_Guard)
# print("Forward", len(Ranked_Forward), Ranked_Forward)
# print("Center", len(Ranked_Center), Ranked_Center)
print()
print()

#generate master list sorted by position and score rating
i = 0
for i in range(no_players):
	if(len(Ranked_Center) > 0):
		Ranked_Masterlist.append(Ranked_Center.pop())
	if(len(Ranked_Forward) > 0):
		Ranked_Masterlist.append(Ranked_Forward.pop())
	if(len(Ranked_Guard) > 0):
		Ranked_Masterlist.append(Ranked_Guard.pop())
	# print(i, len(Ranked_Masterlist), Ranked_Masterlist)

Ranked_Masterlist.reverse() # reverse the list to pop from last record

#seeding of players to teams
batches = math.ceil(int(no_players)/int(team_number))
if batches % 2 != 0:
	batches = batches + 1

Team_Composition = []

i = 0
for i in range(batches):
	x = 0
	for x in range(int(team_number)):
		if len(Ranked_Masterlist) > 0:
			Team_Composition.append([x, Ranked_Masterlist.pop()])
	for y in range(int(team_number)):
		if len(Ranked_Masterlist) > 0:
			Team_Composition.append([int(team_number) - y - 1, Ranked_Masterlist.pop()])

print("\n".join(map(str, Team_Composition)))

# remove target path file if previously exisiting
try:
	os.remove(target_path)
except OSError:
	pass
csvRow = ["Team Number", "Sequence Number", "Name", "Position", "Ranking"]
with open(target_path, "a", newline='') as fp:
	wr = csv.writer(fp, dialect='excel')
	wr.writerow(csvRow)

# out = csv.writer(open(target_path, "w"), delimiter=',', quoting=csv.QUOTE_ALL)
# out.writerow(Team_Composition[0][0])


# l = [[2,2,2],[3,3,3],[4,4,4]]
# for i1, inner_l in enumerate(l):
# 	for i2, item in enumerate(inner_l):
# 		print(i1, i2, item, l[i1][i2])
print()
print(Team_Composition[0][1])

i = 0
for i in range(int(team_number)):
	x = 0
	for x in range(no_players):
		if Team_Composition[x][0] == i:
			placeholder = Team_Composition[x][1].copy()
			print("Team Number ", Team_Composition[x][0] + 1, placeholder[0], placeholder[1], placeholder[2], placeholder[3])
			csvRow = [Team_Composition[x][0] +1 , placeholder[0], placeholder[1], placeholder[2], placeholder[3]]
			with open(target_path, "a", newline='') as fp:
				wr = csv.writer(fp, dialect='excel')
				wr.writerow(csvRow)
			del Team_Composition[x][0]
