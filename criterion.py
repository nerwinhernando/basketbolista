
class Criterion(object):
    """Criterion
    following properties:

    Attributes:
        height: 
        weight:
        playing_years:
        achievement:
        total:
    """

    def __init__(self, player_list):
        self.player_list = player_list
        self.height_criterion = []
        self.weight_criterion = []
        self.playing_years_criterion = []
        self.achievement_criterion = []

    def compute_height_score(self):
        # height score computation

        for player in self.player_list:
            p_height = player.height
            
            if p_height <= 148:
                player.height_criterion = 30
            elif 149 <= p_height <= 157:
                player.height_criterion = 40
            elif 158 <= p_height <= 166:
                player.height_criterion = 50
            elif 167 <= p_height <= 175:
                player.height_criterion = 60
            elif 176 <= p_height <= 185:
                player.height_criterion = 70
            elif 186 <= p_height <= 194:
                player.height_criterion = 80
            elif 195 <= p_height <= 202:
                player.height_criterion = 90
            elif p_height >= 203:
                player.height_criterion = 100

    def compute_weight_score(self):
        for player in self.player_list:
            p_height = player.height
            p_weight = player.weight
            
            if (p_weight/((p_height/100)*(p_height/100))) <= 18:  # bmi - extremely underweight
                player.weight_criterion = 40 
            elif (19 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 24):  # bmi - underweight
                player.weight_criterion = 60
            elif (25 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 29):  # bmi - healthy
                player.weight_criterion = 100
            elif (30 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 34):  # bmi - overweight
                player.weight_criterion = 80
            elif (35 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 39):  # bmi - obese
                player.weight_criterion = 60
            elif (p_weight/((p_height/100)*(p_height/100))) >= 40:  # bmi - extremely obese
                player.weight_criterion = 40

    def compute_years_playing_score(self):
        for player in self.player_list:
            p_playing_years = player.playing_years

            if p_playing_years.upper() == str("1-2 years").upper():
                player.playing_years_criterion = 40
            elif p_playing_years.upper() == str("3-5years").upper():
                player.playing_years_criterion = 60
            elif p_playing_years.upper() == str("6-10 years").upper():
                player.playing_years_criterion = 80
            elif p_playing_years.upper() == str("11 years above").upper():
                player.playing_years_criterion = 100

    def compute_past_achievement_score(self):
        for player in self.player_list:
            p_achievment = player.achievement

            if p_achievment.upper() == str("None").upper():
                player.achievement_criterion = 40
            elif p_achievment.upper() == str("Individual Awardee (ROY, Most Improved, etc.)").upper():
                player.achievement_criterion = 60
            elif p_achievment.upper() == str("Mythical 5 member").upper():
                player.achievement_criterion = 80
            elif p_achievment.upper() == str("MVP").upper():
                player.achievement_criterion = 100

    def compute_total_score(self):
        # total score computation
        for player in self.player_list:
            player.total_criterion =    (0.30 * player.height_criterion) + \
                                        (0.20 * player.weight_criterion) + \
                                        (0.20 * player.playing_years_criterion) + \
                                        (0.30 * player.achievement_criterion)

    def display_height_score(self):
        print("Height Score Information")

    def display_weight_score(self):
        print("Weight Score Information")