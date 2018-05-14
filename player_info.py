class PlayerInfo(object):
    """A player info of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        title: 
        name:
        age:
        home_address:
    """

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.title = kwargs['title']
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.home_address = kwargs['home_address']
        self.contact_nos = kwargs['contact_nos']
        self.weight = kwargs['weight']
        self.height = kwargs['height']
        self.position = kwargs['position']
        self.playing_years = kwargs['playing_years']
        self.achievement = kwargs['achievement']
        self.thankyou_page = kwargs['thankyou_page']
        self.thankyou_all = kwargs['thankyou_all']
        self.id = kwargs['ID']
        self.created_date = kwargs['created_date']
        self.updated_date = kwargs['updated_date']
        self.owner = kwargs['owner']

        # criterions
        self.total_criterion = 0
        self.height_criterion = 0
        self.weight_criterion = 0
        self.playing_years_criterion = 0
        self.achievement_criterion = 0

        self.display_info(kwargs)

    def display_info(self, kwargs):
        """Display information about the player """
        print("Player Information")
        print(kwargs)
