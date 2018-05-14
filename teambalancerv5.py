import math
import csv
import os
from player_info import PlayerInfo
from criterion import Criterion


def get_number_of_teams():
	print("Getting Team Numbers for Balancing")
	# text_file = open('input_parameters/team_number.txt', 'r')
	# team_number = text_file.readline().replace('\n', '')
	team_number = 8
	print("Teams for balancing is " + str(team_number))
	# text_file.close()
	return team_number


def locate_source_file_path():
	print("Getting Filepath")
	# text_file = open('input_parameters/file_path.txt', 'r')
	# file_path = text_file.readline().replace('\n', '')
	file_path = "./data/LigaDatabase.csv"
	print("File path is " + file_path)
	# text_file.close()
	return file_path


def get_destination_file_path():
	print("Getting Target Destination of Results")	
	# text_file = open('input_parameters/target_path.txt', 'r')
	# target_path = text_file.readline().replace('\n', '')
	target_path = "data\GroupingsFinal.csv"
	print("Target path is " + target_path)
	# text_file.close()
	return target_path


def parse_liga_csv_file(file_path):
	print("Getting Raw Data form CSV File")
	
	index = 0
	player_list = []

	with open(file_path, 'r') as csv_file:
		csv_file = csv.reader(csv_file)
		next(csv_file)

		for line in csv_file:
			player_info = PlayerInfo(title=str(line[0]), name = str(line[1]), age = int(line[2]), home_address = str(line[3]), \
				contact_nos = str(line[4]), weight = int(line[5]), height = int(line[6]), position = str(line[7]), \
				playing_years = str(line[8]), achievement = str(line[9]), thankyou_page = str(line[10]), thankyou_all = str(line[11]), \
				ID = str(line[12]), created_date = str(line[13]) , updated_date = str(line[14]), owner = str(line[15]))
			player_list.append(player_info)
			index = index + 1

	print("total Records: ", index)
	return player_list


def group_positions(player_list):	
	Position_Center = []
	Position_Forward = []
	Position_Guard = []

	# group by position
	for player in player_list:
		position = player.position.upper()
		if position == str("Guard").upper():
			Position_Guard.append([player.id, player.name.upper(), position, player.total_criterion])
		elif position == str("Forward").upper():
			Position_Forward.append([player.id, player.name.upper(), position, player.total_criterion])
		elif position == str("Center").upper():
			Position_Center.append([player.id, player.name.upper(), position, player.total_criterion])
		# print(ID[i], Name[i], Position[i], Criterion_Total[i])

	return Position_Center, Position_Forward, Position_Guard


def rank(no_players, Ranked_Center, Ranked_Forward, Ranked_Guard):
	Ranked_Masterlist = []
	# rank descending by position
	print("Guard", len(Ranked_Guard), Ranked_Guard)
	print("Forward", len(Ranked_Forward), Ranked_Forward)
	print("Center", len(Ranked_Center), Ranked_Center)
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

	return Ranked_Masterlist


#seeding of players to teams
def seed_players(no_players, team_number, Ranked_Masterlist):
	Team_Composition = []

	batches = math.ceil(int(no_players)/int(team_number))
	if batches % 2 != 0:
		batches = batches + 1
	
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


def balance_team(file_path, no_of_teams, target_path):
	# read the liga csv file exported from the database
	player_list = parse_liga_csv_file(file_path)

	criterion = Criterion(player_list)
	criterion.compute_height_score()
	criterion.compute_weight_score()
	criterion.compute_years_playing_score()
	criterion.compute_past_achievement_score()

	criterion.compute_total_score()

	Position_Center, Position_Forward, Position_Guard = group_positions(player_list)

	ranked_guard = sorted(Position_Guard, key=lambda x: x[3], reverse=False)
	ranked_forward = sorted(Position_Forward, key=lambda x: x[3], reverse=False)
	ranked_center = sorted(Position_Center, key=lambda x: x[3], reverse=False)

	rank(len(player_list), ranked_center, ranked_forward, ranked_guard)

	#seed_players(len(player_list), no_of_teams, target_path)


if __name__ == '__main__':
    no_of_teams = get_number_of_teams()
    source_file_path = locate_source_file_path()
    destination_file_path = get_destination_file_path()

    balance_team(source_file_path, no_of_teams, destination_file_path)

