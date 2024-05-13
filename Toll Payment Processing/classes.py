class Toll:
    def __init__(self, tollName, ischargeable, payment):
        self.name = tollName
        self.ischargeable = ischargeable
        self.vechicleDetails = []
        self.revenue = 0
        self.payment = payment