
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
                self.height_criterion.append(30)
            elif 149 <= p_height <= 157:
                self.height_criterion.append(40)
            elif 158 <= p_height <= 166:
                self.height_criterion.append(50)
            elif 167 <= p_height <= 175:
                self.height_criterion.append(60)
            elif 176 <= p_height <= 185:
                self.height_criterion.append(70)
            elif 186 <= p_height <= 194:
                self.height_criterion.append(80)
            elif 195 <= p_height <= 202:
                self.height_criterion.append(90)
            elif p_height >= 203:
                self.height_criterion.append(100)

    def compute_weight_score(self):
        for player in self.player_list:
            p_height = player.height
            p_weight = player.weight
            
            if (p_weight/((p_height/100)*(p_height/100))) <= 18:  # bmi - extremely underweight
                self.weight_criterion.append(40)
            elif (19 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 24):  # bmi - underweight
                self.weight_criterion.append(60)
            elif (25 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 29):  # bmi - healthy
                self.weight_criterion.append(100)
            elif (30 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 34):  # bmi - overweight
                self.weight_criterion.append(80)
            elif (35 <= (p_weight/((p_height/100)*(p_height/100)))) and (p_weight/((p_height/100)*(p_height/100)) <= 39):  # bmi - obese
                self.weight_criterion.append(60)
            elif (p_weight/((p_height/100)*(p_height/100))) >= 40:  # bmi - extremely obese
                self.weight_criterion.append(40)

    def compute_years_playing_score(self):
        for player in self.player_list:
            p_playing_years = player.playing_years

            if p_playing_years.upper() == str("1-2 years").upper():
                self.playing_years_criterion.append(40)
            elif p_playing_years.upper() == str("3-5years").upper():
                self.playing_years_criterion.append(60)
            elif p_playing_years.upper() == str("6-10 years").upper():
                self.playing_years_criterion.append(80)
            elif p_playing_years.upper() == str("11 years above").upper():
                self.playing_years_criterion.append(100)

    def compute_past_achievement_score(self):
        for player in self.player_list:
            p_achievment = player.achievement

            if p_achievment.upper() == str("None").upper():
                self.achievement_criterion.append(40)
            elif p_achievment.upper() == str("Individual Awardee (ROY, Most Improved, etc.)").upper():
                self.achievement_criterion.append(60)
            elif p_achievment.upper() == str("Mythical 5 member").upper():
                self.achievement_criterion.append(80)
            elif p_achievment.upper() == str("MVP").upper():
                self.achievement_criterion.append(100)

    def display_height_score(self):
        print("Height Score Information")

    def display_weight_score(self):
        print("Weight Score Information")