
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

    def display_info(self, kwargs):
        """Display information about the criterion """
        print("Information")
